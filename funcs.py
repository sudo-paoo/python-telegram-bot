from dotenv import load_dotenv
import os
import requests
import json
import telebot

# LOAD ENVIRONMENT VARIABLES

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')
QR_URL = os.getenv('QR_URL')
NASA_API = os.getenv('NASA_API')
NASA_URL = os.getenv('NASA_URL')
U_FACTS = os.getenv('U_FACTS')

# BOT 

bot = telebot.TeleBot(TG_TOKEN)
commands = ['define', 'tiktokdl', 'apod', 'ufacts', 'smovie', 'horoscope']


#START MESSAGE / ALIVE OR NOT

def start_msg(message):
    first_name = message.chat.first_name
    bot.send_message(message.chat.id, f"""
Hi {first_name}, I'm alive
*Dumm E*
/help for the list of my commands
*Made By:* @sudopao
*Language:* _Python_ 
*Framework:* _Telebot_""", parse_mode='Markdown')


# HELP MESSAGE

def help_msg(message):
    bot.send_message(message.chat.id, text=f"""
Commands:
/start
📖Check if my alive or not
/help
📖Provide an overview of my commands
/apod
📖Provides the Astronomy Picture of the Day
/generateqr
📖Generates a qr code from the given text
/ufacts
📖Send useless facts
""", parse_mode='Markdown')

# NASA PICTURE OF THE DAY

def apod(message):
    if message.text[1:] in commands:
        bot.send_message(message.chat.id, f"The command {'/apod'} has been interrupted. Anything else I can do for you?\n\nSend /help for a list of commands.", parse_mode='Markdown')
    elif message.text == '/help': 
        help_msg(message)    
    elif message.text == '/start':
        start_msg(message)
    else:
        try:
            bot.send_message(message.chat.id, 'Gathering data from NASA.')
            date = message.text
            params = {
            'api_key': NASA_API,
            'hd': 'True',
            'date': date
            }
            resp = requests.get(NASA_URL + NASA_API, params=params)
            respData = json.loads(resp.text)
            date = respData['date']
            title = respData['title']
            explanation = respData['explanation']
            bot.send_chat_action(message.chat.id, action='upload_photo')
            bot.send_photo(message.chat.id, photo=respData['hdurl'], caption=f'*Title: * {title} \n\n*Date: * {date} \n\n*Description:* {explanation}', parse_mode='Markdown')
        except KeyError:
            bot.send_message(message.chat.id, 'There was and error finding the image with the given date. Please try again.')
        except:
            bot.send_message(message.chat.id, 'There is a problem with the first image url. Sending the second image url. Please wait')
            date = message.text
            params = {
            'api_key': NASA_API,
            'hd': 'True',
            'date': date
            }
            resp = requests.get(NASA_URL + NASA_API, params=params)
            respData = json.loads(resp.text)
            date = respData['date']
            title = respData['title']
            explanation = respData['explanation']
            bot.send_chat_action(message.chat.id, action='upload_photo')
            bot.send_photo(message.chat.id, photo=respData['url'], caption=f'*Title: *  {title} \n\n*Date: * {date} \n\n*Description: * {explanation}', parse_mode='Markdown')

# USELESS FACTS

def ufacts(message):
    try:
        uf = requests.get(U_FACTS)
        data = json.loads(uf.text)
        bot.send_message(message.chat.id, text='*Useless Fact:* \n\n' + data['text'], parse_mode='Markdown')
    except:
        bot.send_message(message.chat.id, 'Sorry there was an error finding a  useless fact. Please try again.')

#GENERATE QR CODE

def generateqr(message):
    if message.text[1:] in commands:
        bot.send_message(message.chat.id, f"The command {'/generateqr'} has been interrupted. Anything else I can do for you?\n\nSend /help for a list of commands.", parse_mode='Markdown')
    elif message.text == '/help': 
        help_msg(message)    
    elif message.text == '/start':
        start_msg(message)
    else:
        bot.send_message(message.chat.id, "Generating QR Code.")
        data = message.text
        qr_code = QR_URL + data
        bot.send_photo(message.chat.id, photo=qr_code)
