#Join me at telegram @dev_gagan

from pyrogram import Client
from pyromod import listen
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID ="15578503"
API_HASH ="de14eccfa6fa8d7c2eee9656cc2bdc69"
BOT_TOKEN ="7501679052:AAFhMm4dtaXIcRiY4tBXn54tguj1H9CzCeg"
SESSION ="BQDttYcAB7XpUoi-dY4m_5YPbcyoJm5L51BIjIWQH2IMAYVnzTtytKU3513SZncor5-SrCf-VqLAsN5J6SoT0L4NSlwqTNEkoPxkaKqHCgYUjnPkIAZY8O2jGSssrzWwTyBt8EQMzT53kTfNQxieGra6AIhPGgqUgZcw6t5p0BVf4YJxM32MljPOqOjjFLImzBvMMq1rSnUbxKvHhTvYhQnGKj5MFgOjpHU2MUEaQiJLvoxg4T97nDO-bxYa4DzZZ3zXCQVcAPSegk3T3zevrHI79DcWdcoVt-Kw-kv2EQ_0HCyo9hT6Yp-2jKrziD9YonlaZLok7xWGfrto3kHbZqtFXPMIvQAAAAFJWkbdAA"
FORCESUB ="AtulChannelhainbhai"
AUTH ="5525620445"
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
