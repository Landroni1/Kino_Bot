from telebot import types
from loader import bot
from states.search_states import search_active

def bot_keyboard_stop():
    stop_kb = types.InlineKeyboardMarkup()
    stop_kb_1 = types.InlineKeyboardButton(text='Да ✅', callback_data='stop')
    stop_kb_2 = types.InlineKeyboardButton(text='Нет ❌', callback_data='search')
    return stop_kb.add(stop_kb_1, stop_kb_2)

@bot.callback_query_handler(func=lambda call: call.data == "stop")
def stop_callback(call):
    search_active.pop(call.from_user.id, None)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="✅ Поиск отменён!",
        reply_markup=None
    )

@bot.callback_query_handler(func=lambda call: call.data == "search")
def search_callback(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🔍 Продолжаем поиск"
             "\nВведите название фильма:",
        reply_markup=None
    )



def bot_keyboard_search_cancel():
    cancel_kb = types.InlineKeyboardMarkup()
    cancel_kb_1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
    return cancel_kb.add(cancel_kb_1)

@bot.callback_query_handler(func=lambda call: call.data == "cancel")
def stop_callback(call):
    search_active.pop(call.from_user.id, None)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="✅ Поиск отменён!",
        reply_markup=None
    )

