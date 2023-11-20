#!/usr/bin/env python

import psutil
import telebot

# Replace YOUR_BOT_TOKEN with your actual bot token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Trigger words
trigger_words = ['/cpu', '/ram', '/storage', '/help']

# Get the CPU load
def get_cpu_load():
    return psutil.cpu_percent()

# Get the RAM usage
def get_ram_usage():
    return psutil.virtual_memory().percent

# Get the storage usage
def get_storage_usage():
    return psutil.disk_usage('/').percent

# Send the CPU load to the Telegram bot
def send_cpu_load(chat_id):
    cpu_load = get_cpu_load()
    message = f"Current CPU load: {cpu_load}%"
    bot.send_message(chat_id, message)

# Send the RAM usage to the Telegram bot
def send_ram_usage(chat_id):
    ram_usage = get_ram_usage()
    message = f"Current RAM usage: {ram_usage}%"
    bot.send_message(chat_id, message)

# Send the storage usage to the Telegram bot
def send_storage_usage(chat_id):
    storage_usage = get_storage_usage()
    message = f"Current storage usage: {storage_usage}%"
    bot.send_message(chat_id, message)

# Send the list commands to the Telegram bot
def send_help(chat_id):
    message = "Available commands: /cpu, /ram, /storage"
    bot.send_message(chat_id, message)

# Define the function to handle incoming messages
@bot.message_handler(func=lambda message: message.text in trigger_words)
def handle_message(message):
    chat_id = -4073498824 # Replace YOUR_CHAT_ID with the actual chat ID where you want to send the message
    if message.text == '/cpu':
        send_cpu_load(chat_id)
    elif message.text == '/ram':
        send_ram_usage(chat_id)
    elif message.text == '/storage':
        send_storage_usage(chat_id)
    elif message.text == '/help':
        send_help(chat_id)

# Start the bot
while True:
    try:
        bot.polling()
    except Exception:
        continue