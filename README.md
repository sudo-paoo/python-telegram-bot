# Python-Telegram-Bot (DUMM-E)

This is a python telegram bot made with pyTelegramBotAPI framework. Telegram has announced official support for a [Bot API](https://telegram.org/blog/bot-revolution), which will allow all types of integrators to introduce automated interactions to the mobile platform.


## Bot Commands

| Commands    	| Functions                             	| User Input              	|
|-------------	|------------------------------------------	|------------------------	|
| /start      	| checking if the bot is online             | None                    	|
| /help       	| sends the list of all available commands  | None                    	|
| /apod       	| provide the astronomy picture of the day  | <YYYY-MM-DD> format     	|
| /generateqr 	| sends a qr code to the given text         | text                    	|
| /ufact      	| sends a useless fact                      | None                    	|



## Installing modules

- [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html)
  - Framework
```python
    pip install pyTelegramBotAPI
```
-  [dotenv](https://github.com/theskumar/python-dotenv)
    - environment variables
```python
    pip install python-dotenv
```

## APIs

- Generating QR Code --> [goqr](https://goqr.me/api/)
- Astronomy Picture of the Day by NASA --> [NASA](https://api.nasa.gov/)
- Useless Facts --> [useless](https://uselessfacts.jsph.pl/)
