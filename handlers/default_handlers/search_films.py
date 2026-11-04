from telebot.types import InlineKeyboardMarkup, Message # noqa

from api.kinopoisk import get_movie_data
from keyboards.stop_kb import bot_keyboard_search_cancel, bot_keyboard_stop
from loader import bot
from states.search_states import MovieStates
from utils.text_utils import clean_rating, clean_text


@bot.message_handler(commands=["search_films"])
@bot.message_handler(func=lambda message: message.text == "Поиск фильмов 🔍")
def bot_search_films(message: Message):
    if message.from_user is not None:
        bot.set_state(message.from_user.id, MovieStates.wait_for_title, message.chat.id)
    bot.send_message(
        message.chat.id,
        "Введите название фильма:",
        reply_markup=bot_keyboard_search_cancel(),
    )


@bot.message_handler(state=MovieStates.wait_for_title)
def process_movie_search(message):
    query = message.text

    if query.startswith("/"):
        bot.delete_state(message.from_user.id, message.chat.id)
        return

    bot.send_message(message.chat.id, "Ищу {title} ...".format(title=query))

    movies = get_movie_data(query)

    if movies:
        for movie in movies:
            title = (
                movie.get("name")
                or movie.get("alternativeName")
                or "Название неизвестно"
            )
            year = movie.get("year", "---")
            rating = clean_rating(movie.get("rating", {}).get("kp", "Нет"))
            description = clean_text(movie.get("description", "Описание не найдено"))
            if movie and movie.get("poster"):
                poster_url = movie["poster"].get("url")
            else:
                poster_url = None

            caption = (
                "{title} - {year}"
                "\nРейтинг - {rating}"
                "\n{description}".format(
                    title=title, year=year, rating=rating, description=description
                )
            )

            if poster_url:
                try:
                    bot.send_photo(
                        message.chat.id, poster_url, caption=caption, parse_mode=None
                    )
                except Exception as e:
                    print(f"Не удалось отправить постер: {e}")
                    bot.send_message(message.chat.id, caption, parse_mode=None)
            else:
                bot.send_message(message.chat.id, caption, parse_mode=None)
    else:
        bot.send_message(
            message.chat.id, "Ничего не найдено. Попробуйте уточнить название."
        )

    bot.send_message(
        message.chat.id, "Желаете остановить поиск?", reply_markup=bot_keyboard_stop()
    )
