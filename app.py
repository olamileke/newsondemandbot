from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from endpoints import call_endpoint
import os.path as path
import logging
import config
import json

# Enable logging of errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Creating the relevant variables
updater = Updater(
    token=config.bot_token, use_context=True)
dispatcher = updater.dispatcher

# Handler Functions
def start(update, context):
    with open(path.join(config.base_directory, 'start_message.txt')) as reader:
        text = reader.read()

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def get(update, context):
    article = call_endpoint()
    chat_id = update.effective_chat.id
    url = article['url']
    source_text = "<a href='{0}'>Read more</a>".format(url)
    context.bot.send_message(chat_id=chat_id, text=article['title'])
    if article['content'] is not None:
        context.bot.send_message(chat_id=chat_id, text=article['content'])
    context.bot.send_message(
        chat_id=chat_id, text=source_text, parse_mode=ParseMode.HTML)


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm sorry. I do not understand that")


# Creating the handlers
start_handler = CommandHandler('start', start)
get_handler = CommandHandler('get', get)
unknown_handler = MessageHandler(Filters.all, unknown)


# Adding the handlers to the dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_handler)
dispatcher.add_handler(unknown_handler)

# Starting the bot
updater.start_polling()