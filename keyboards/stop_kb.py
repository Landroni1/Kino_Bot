from telebot import types
from loader import bot


def bot_keyboard_stop():
    stop_kb = types.InlineKeyboardMarkup()
    stop_kb_1 = types.InlineKeyboardButton(text='Да ✅', callback_data='stop')
    stop_kb_2 = types.InlineKeyboardButton(text='Нет ❌', callback_data='search')
    return stop_kb.add(stop_kb_1, stop_kb_2)

def bot_keyboard_search_cancel():
    cancel_kb = types.InlineKeyboardMarkup()
    cancel_kb_1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
    return cancel_kb.add(cancel_kb_1)


