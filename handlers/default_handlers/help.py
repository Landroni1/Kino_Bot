from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot

@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == 'Помощь ⁉️')
def bot_help(message: Message):
    text = ['{command} {text_command}'.format(command=command, text_command=desk) for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, '\n'.join(text))


