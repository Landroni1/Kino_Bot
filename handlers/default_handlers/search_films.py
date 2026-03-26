from telebot.types import Message, InlineKeyboardMarkup
from api.kinopoisk import get_movie_data
from loader import bot
from utils.text_utils import clean_text, clean_rating
from keyboards.stop_kb import bot_keyboard_stop, bot_keyboard_search_cancel
from states.search_states import search_active

@bot.message_handler(commands=['search_films'])
def bot_search_films(message: Message):
    search_active[message.from_user.id] = True
    bot.send_message(message.chat.id,'Введите название фильма:', reply_markup=bot_keyboard_search_cancel())

@bot.message_handler(func=lambda message: message.text == 'Поиск фильмов 🔍')
def bot_search_films(message: Message):
    search_active[message.from_user.id] = True
    bot.send_message(message.chat.id,'Введите название фильма:', reply_markup=bot_keyboard_search_cancel())

@bot.message_handler(func=lambda message: (
    message.from_user.id in search_active and      # В режиме поиска
    not message.text.startswith('/')
    and message.text not in ['Поиск фильмов 🔍']        # НЕ кнопка меню
))
def search_films(message: Message):
    search_active[message.from_user.id] = False
    query = message.text
    bot.send_message(message.chat.id, 'Ищу {title}....'.format(title=query))

    movie = get_movie_data(query)

    #Получше разобраться в этих значениях
    if movie:
        title = movie.get('name') or movie.get('alternativeName') or 'Название неизвестно'
        year = movie.get('year', '---')
        rating = clean_rating(movie.get('rating', {}).get('kp', 'Нет'))
        description = clean_text(movie.get('description', 'Описание не найдено'))
        poster_url = movie.get('poster', {}).get('url')

        caption = (
            '{title} - {year}'
            '\nРейтинг - Х{rating}'
            '\n{description}'.format(title=title, year=year, rating=rating, description=description)
        )

        if poster_url:
            bot.send_photo(message.chat.id, poster_url, caption=caption, parse_mode=None)
        else:
            bot.send_message(message.chat.id, caption, parse_mode=None)
    else:
        bot.send_message(message.chat.id, 'Ничего не найдено. Попробуйте уточнить название.')

    bot.send_message(message.chat.id, 'Желаете остановить поиск?', reply_markup=bot_keyboard_stop())