#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


#configs for the bot
from plugins.helpers.config import Config

from telegram import ParseMode


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


import os

import telegram

#Configs for the bot

from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler, Filters






startt_handler = CommandHandler('start', start)

attach_handler = MessageHandler(Filters.text, attach)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(attach_handler)


def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi [{update.message.from_user.first_name}](tg://user?id={update.message.from_user.id}) I am Attach Bot. I can attach medias to your long text.", parse_mode="Markdown")


def attach(update, context):
  if update.message.reply_to_message == None:
    update.message.reply_text("Reply to a media to get an attached Media")
  else:
    m = context.bot.forward_message("@" + Config.CHANNEL_USERNAME, update.effective_chat.id, update.message.reply_to_message.message_id)
    m_id = m.message_id
    link = "https://t.me/{}/{}".format(Config.CHANNEL_USERNAME, m_id)
    print(link)
    context.bot.send_message(update.effective_chat.id, update.message.text + "[{}]({})".format("\u2063", link), parse_mode=ParseMode.MARKDOWN)



updater.start_polling()
