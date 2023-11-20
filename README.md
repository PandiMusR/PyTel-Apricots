# PyTel-Apricots

This Python script uses the `psutil` and `telebot` libraries to monitor system resources and send the data to a Telegram bot.

## Features

- Monitor CPU load
- Monitor RAM usage
- Monitor storage usage

## How it works

The script defines several functions to retrieve system resource usage:

- `get_cpu_load()`: Returns the current CPU load as a percentage.
- `get_ram_usage()`: Returns the current RAM usage as a percentage.
- `get_storage_usage()`: Returns the current storage usage as a percentage.

These functions are then used to send messages to a Telegram bot with the current resource usage.

## Setup

Replace `YOUR_BOT_TOKEN` with your actual bot token in the line:

```python
bot = telebot.TeleBot('YOUR_BOT_TOKEN')
chat_id = 'YOUR_CHAT_ID'
```

## Usage

Send one of the following commands to the Telegram bot:

- `/cpu`: Returns the current CPU load.
- `/ram`: Returns the current RAM usage.
- `/storage`: Returns the current storage usage.
- `/help`: Returns a help message.

## Note

Sometimes the output of CPU load is `0.0%`. This is because the `psutil` library returns the CPU load as a float with one decimal place, you can send more than one message to the Telegram bot to see the actual CPU load.
