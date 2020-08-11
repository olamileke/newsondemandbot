from telegram import ParseMode, ChatAction
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


def get(update, context, article=None):

    chat_id = str(update.effective_chat.id)

    if article is None:
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        article = call_endpoint()
        save(article, chat_id)


    url = article['url']
    source_text = "<a href='{0}'>Read more</a>".format(url)
    context.bot.send_message(chat_id=chat_id, text=article['title'])

    if article['content'] is not None:
        context.bot.send_message(chat_id=chat_id, text=article['content'])
    context.bot.send_message(
        chat_id=chat_id, text=source_text, parse_mode=ParseMode.HTML)


def save(article, chat_id):
    with open(path.join(config.base_directory, 'stored_alerts.json')) as reader:
        stored_alerts = json.load(reader)

    if chat_id in stored_alerts:
        stored_alerts[chat_id].append(article)
    else:
        stored_alerts[chat_id] = []
        stored_alerts[chat_id].append(article)

    with open(path.join(config.base_directory, 'stored_alerts.json'), 'w') as writer:
        json.dump(stored_alerts, writer)

    return

def history(update, context):
    chat_id = str(update.effective_chat.id)
    with open(path.join(config.base_directory, 'stored_alerts.json')) as reader:
        stored_alerts = json.load(reader)

    if chat_id not in stored_alerts:
        context.bot.send_message(chat_id=chat_id, text="I haven't sent you any article apparently")
        return        

    articles = stored_alerts[chat_id]
    num_articles = len(articles)

    for i in range(0, num_articles):
        get(update, context, articles[i])


def clear(update, context):
    chat_id = str(update.effective_chat.id)

    with open(path.join(config.base_directory, 'stored_alerts.json')) as reader:
        stored_alerts = json.load(reader)

    if chat_id not in stored_alerts:
        return context.bot.send_message(chat_id=chat_id, text="You do not a history to clear!")

    del stored_alerts[chat_id]

    with open(path.join(config.base_directory, 'stored_alerts.json'), 'w') as writer:
        json.dump(stored_alerts, writer)

    context.bot.send_message(chat_id=chat_id, text='History cleared successfully!')


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm sorry. I do not understand that")


# Creating the handlers
start_handler = CommandHandler('start', start)
get_handler = CommandHandler('get', get)
history_handler = CommandHandler('history', history)
clear_handler = CommandHandler('delete', clear)
unknown_handler = MessageHandler(Filters.all, unknown)


# Adding the handlers to the dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_handler)
dispatcher.add_handler(history_handler)
dispatcher.add_handler(clear_handler)
dispatcher.add_handler(unknown_handler)

# Starting the bot
updater.start_polling()
updater.idle()