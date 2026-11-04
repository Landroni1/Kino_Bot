from telebot.types import Message

from keyboards.start_kb import bot_keyboard_start
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user_name = message.from_user.full_name if message.from_user else "Гость"
    bot.reply_to(
        message,
        "Привет👋\nРад познакомиться с тобой {user_name} ☺️"
        "\nЯ — твой бот по поиску фильмов 🤖"
        "\nСейчас я похож на новорожденного: много сплю и мало что умею. "
        "\nМой создатель вовсю пишет код, чтобы я стал умнее."
        "\nПока что ты можешь протестировать мою базовую систему командами:"
        "\n/search_films и /help"
        "\nЛибо нажать на кнопки внизу.".format(user_name=user_name),
        reply_markup=bot_keyboard_start(),
    )
