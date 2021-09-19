from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import MessageFilter, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Updater
updater = Updater(token="YOUR BOT TOKEN HERE")
dispatcher = updater.dispatcher

# Start function
def start(update, context) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text="Hello, I am Rajasthani Bot!")

# echo function
def echo(update, context) -> None:
    user_message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text=user_message)

# inline command
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(id=query.upper(),
        title="Caps",
        input_message_content=InputTextMessageContent(query.upper()))
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

# Unknown Command
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="There is no such command!")

# Handler
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
inline_caps_handler = InlineQueryHandler(inline_caps)
unknown_handler = MessageHandler(Filters.command, unknown)

# Dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()

