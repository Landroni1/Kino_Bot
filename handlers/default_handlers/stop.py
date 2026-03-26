from telebot.types import Message
from states.search_states import search_active
from loader import bot

@bot.message_handler(commands=['stop'])
def cancel_search(message: Message):
    search_active.pop(message.from_user.id, None)
    bot.reply_to(message, '✅ Поиск отменён!')