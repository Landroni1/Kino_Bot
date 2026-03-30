from loader import bot
from utils.set_bot_commands import set_default_commands
from telebot import custom_filters
import handlers


if __name__ == '__main__':
    set_default_commands(bot)
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling(skip_pending=True)
    bot.infinity_polling()
