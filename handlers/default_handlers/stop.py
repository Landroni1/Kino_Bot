from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["stop"])
def cancel_search(message: Message):
    if message.from_user is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
    bot.reply_to(message, "✅ Поиск отменён!")
