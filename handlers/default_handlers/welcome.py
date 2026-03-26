from telebot import types

from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(content_types=['text'])
def bot_echo(message: types.Message):
    bot_name = bot.get_me().username
    if message.text.strip().lower().startswith('привет'):
        bot.reply_to(
            message, 'Хей! Рад тебя снова видеть 👋'
                     '\nЯ еще совсем «зеленый» и только учусь взаимодействовать с миром.'
                     '\nЗаглядывай чуть позже, когда я обрасту новыми фичами!'
                     '\nА пока, держи все что я умею:'
                     '\n/search_films'
                     '\n/hello_world'
        )
