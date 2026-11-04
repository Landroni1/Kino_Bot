from telebot import types

from loader import bot


@bot.message_handler(
    func=lambda message: message.text.strip().lower().startswith("привет")
)
def bot_echo(message: types.Message):
    bot.reply_to(
        message,
        "Хей! Рад тебя снова видеть 👋"
        "\nЯ еще совсем «зеленый» и только учусь взаимодействовать с миром."
        "\nЗаглядывай чуть позже, когда я обрасту новыми фичами!"
        "\nА пока, держи все что я умею:"
        "\n/search_films"
        "\n/hello_world",
    )
