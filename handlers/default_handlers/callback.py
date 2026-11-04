from loader import bot
from states.search_states import MovieStates # noqa


@bot.callback_query_handler(func=lambda call: call.data == "stop")
def stop_callback(call):
    bot.delete_state(call.from_user.id, call.message.chat.id)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="✅ Поиск отменён!",
        reply_markup=None,
    )


@bot.callback_query_handler(func=lambda call: call.data == "search")
def search_callback(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🔍 Продолжаем поиск" "\nВведите название фильма:",
        reply_markup=None,
    )


@bot.callback_query_handler(func=lambda call: call.data == "cancel")
def cancel_callback(call):
    bot.delete_state(call.from_user.id, call.message.chat.id)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="✅ Поиск отменён!",
        reply_markup=None,
    )
