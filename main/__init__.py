#Join me at telegram @dev_gagan

from pyrogram import Client
from pyromod import listen
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "15663518"
API_HASH = "d675b3e5ad6fcf248d6ddafc8c07c53b"
BOT_TOKEN = "8163129853:AAG3RimnlpjWdD9FHdXEM_gk_sL3T51rvrc"
SESSION = "BQDvAZ4AUPk2WgGR9V-R7k00wqR2d_4FKV3HCaZM_ZLF9OhfB0KM4KrKfWsDTtU4VDAiCfOobY5-8qLiuXYBIM1AV2C7SetUg4kImLOfzYkboxAWToS41hLSmrSzJhKAxf3jSIPx4WIZqFWabknxTV8gNelVjIeMlok_VyKf3X8AM5GkmiGDJGdH6ZbXSR5dVr9cZmv1utCyxjDm7Nuu21W21IbSK0eMSxgp0owkhSFSWbjN6CWBAoQiiaDuGapaWLMsKpuute4y3KlvUtxBbaMtn2mEKRHJjH0s2q-vL8JqtagT1h4CTsYPHTqVt3C5jyYDd1G4bchEXh_dfk8M_Yw90whECgAAAAGqNXUWAA"
FORCESUB = "srcbopbothain"
AUTH = "7150597398"
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
userbot = Client("myacc", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @scrpbothainbhai.")
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
