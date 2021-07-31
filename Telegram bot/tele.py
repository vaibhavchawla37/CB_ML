# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 06:52:37 2021

@author: Vaibhav
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN='1727956726:AAHkSEFc43kvsKaVz3MWlkufUkQG9Ljg4kA'


def start(bot,update):
    print(update)
    author = update.message.from_user.first_name
    reply = f"Hi!..{author}"
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def _help(bot,update):
    author = update.message.from_user.first_name
    help_text=f"Hey!{author} I will help you "
    bot.send_message(chat_id=update.message.chat_id,text=help_text)
    
def echo_text(bot,update):
    reply=update.message.text 
    bot.send_message(chat_id=update.message.chat_id,text=reply)
    
def echo_sticker(bot,update):
    reply=update.message.sticker.file_id
    bot.send_sticker(chat_id=update.message.chat_id,sticker=reply)
    
def error(bot,update):
    logger.error("update '%s' caused error '%s'",update,update.error)
    
    
#create updater
def main():
    updater=Updater(TOKEN,use_context=False)
    dp=updater.dispatcher
    
    dp.add_handler(CommandHandler('start',start) )
    dp.add_handler(CommandHandler('help',_help) )
    dp.add_handler(MessageHandler(Filters.text,echo_text) )
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker) )
    dp.add_error_handler(error)
    
    updater.start_polling()
    logger.info("started polling....")
    updater.idle()
    
    
if __name__=="__main__" :
    main()       
