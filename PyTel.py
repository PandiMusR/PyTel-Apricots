#!/usr/bin/env python

import psutil
import telebot

# Replace YOUR_BOT_TOKEN with your actual bot token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Trigger words
trigger_words = '/cpu'

# Get the CPU load
def get_cpu_load():
    return psutil.cpu_percent()

# Send the CPU load to the Telegram bot
def send_cpu_load(chat_id):
    cpu_load = get_cpu_load()
    message = f"Current CPU load: {cpu_load}%"
    bot.send_message(chat_id, message)

# Def to handle incoming messages
@bot.message_handler(func=lambda message: message.text in trigger_words)
def handle_message(message):
    chat_id = YOUR_CHAT_ID # Replace YOUR_CHAT_ID with the actual chat ID where you want to send the message
    if message.text == '/cpu':
        send_cpu_load(chat_id)

# Start the bot
while True:
    try:
        bot.polling()
    except Exception:
        continue
