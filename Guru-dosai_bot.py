from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random


updater = Updater("5553543801:AAF6S3j1zZApELnaQTPX6SJM_QEfRtHjyTc",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Hello Welcome to Guru Dosai please type
        /help for commands""")
    

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/pickup
/delievery""")
    update.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)

x = random.randint(10000,20000)
  
def pickup_order(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Sir May i get your order pls""")
    update.message.reply_text(
        """Sir your order number is"""
    )
    update.message.reply_text(
        x
    )
    update.message.reply_animation('https://c.tenor.com/r_Gf5d2leQQAAAAj/cooking.gif')
    
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('pickup', pickup_order))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()