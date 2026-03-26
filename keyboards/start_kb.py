from telebot import types

def bot_keyboard_start():
    start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_1 = types.KeyboardButton('Поиск фильмов 🔍')
    kb_2 = types.KeyboardButton('Помощь ⁉️')
    return start_kb.add(kb_1, kb_2)
