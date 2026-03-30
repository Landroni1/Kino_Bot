from telebot.handler_backends import State, StatesGroup

class MovieStates(StatesGroup):
    wait_for_title = State()  # Ожидание ввода названия фильма
