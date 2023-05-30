from dotenv import load_dotenv
from funcs import *
import telebot
import os

# LOAD ENVIRONMENT VARIABLES

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')

# BOT

bot = telebot.TeleBot(TG_TOKEN)

commands = ['define', 'apod', 'ufacts', 'generateqr', 'help', 'start']

# START

@bot.message_handler(commands=['start'])
def msg(message):
    start_msg(message)

# HELP

@bot.message_handler(commands=['help'])
def msg(message):
    help_msg(message)

# NASA ASTRONOMY PICTURE OF THE DAY

@bot.message_handler(commands=['apod'])
def msg(message):
    msg = bot.send_message(message.chat.id, 'Send a date to find the NASA image of the day. YYYY-MM-DD format.')
    bot.register_next_step_handler(msg, apod)

# USELESS FACTS

@bot.message_handler(commands=['ufacts'])
def msg(message):
    ufacts(message)

# GENERATE QR CODE

@bot.message_handler(commands=['generateqr'])
def msg(message):
    msg = bot.send_message(message.chat.id, 'Send a text to generate qr code.')
    bot.register_next_step_handler(msg, generateqr)

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()