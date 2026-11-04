from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data import config

assert config.BOT_TOKEN is not None, "BOT_TOKEN не задан в конфигурации!"

storage = StateMemoryStorage()
bot = TeleBot(config.BOT_TOKEN, state_storage=storage)
