from telebot.types import Message, InlineKeyboardMarkup
from api.kinopoisk import get_movie_data
from loader import bot
from utils.text_utils import clean_text, clean_rating
from keyboards.stop_kb import bot_keyboard_stop, bot_keyboard_search_cancel
from states.search_states import MovieStates

@bot.message_handler(commands=['search_films'])
@bot.message_handler(func=lambda message: message.text == 'Поиск фильмов 🔍')
def bot_search_films(message: Message):
    bot.set_state(message.from_user.id, MovieStates.wait_for_title, message.chat.id)
    bot.send_message(message.chat.id,'Введите название фильма:', reply_markup=bot_keyboard_search_cancel())

@bot.message_handler(state=MovieStates.wait_for_title)
def process_movie_search(message):
    query = message.text

    if query.startswith('/'):
        bot.delete_state(message.from_user.id, message.chat.id)
        return

    bot.send_message(message.chat.id, 'Ищу {title} ...'.format(title=query))

    movies = get_movie_data(query)

    #Получше разобраться в этих значениях
    if movies:
        for movie in movies:
            title = movie.get('name') or movie.get('alternativeName') or 'Название неизвестно'
            year = movie.get('year', '---')
            rating = clean_rating(movie.get('rating', {}).get('kp', 'Нет'))
            description = clean_text(movie.get('description', 'Описание не найдено'))
            if movie and movie.get('poster'):
                poster_url = movie['poster'].get('url')
            else:
                poster_url = None

            caption = (
                '{title} - {year}'
                '\nРейтинг - {rating}'
                '\n{description}'.format(title=title, year=year, rating=rating, description=description)
            )

            if poster_url:
                bot.send_photo(message.chat.id, poster_url, caption=caption, parse_mode=None)
            else:
                bot.send_message(message.chat.id, caption, parse_mode=None)
    else:
        bot.send_message(message.chat.id, 'Ничего не найдено. Попробуйте уточнить название.')

    bot.send_message(message.chat.id, 'Желаете остановить поиск?', reply_markup=bot_keyboard_stop())