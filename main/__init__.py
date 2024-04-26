#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "23004101" #config("API_ID", default=None, cast=int)
API_HASH = "a2e157e87728053027cbb156e41a832a" #config("API_HASH", default=None)
BOT_TOKEN = "6878209338:AAHkmzPscKco364oQJsxaURtk9frdqPx81k" #config("BOT_TOKEN", default=None)
SESSION = "BQFfA8UARFESXgzZu7SKvJtOrugeghODnaUGzy-80J_DtwXo8Ey5k-DE-jsPRYVu9HCOiqZM-wcGo11xLrF4CGhacdLoUiKLcQh8cgLRGEHt7XD1LU8PizGrjEBzJ5hIHJpotIxYx-zq2wQcd7C1jJjlpwaAybNnKUwE2CWvJamec4CsLFeRdopjtovwJ3cbBo8vx1c-6Z_S27lR-4Uz6NQ1g2093-iUU4ll8ba9HZc4PmXAOJVsfB9iq_ALbzqGvlodQjZ03j7w_NFX8405EEbjmssVMVnixdO00k_SmxttxeKPe6sxn5pH6UKt20IKKULJcnW4GoxoxAUIrNCCEHqYsh_hZAAAAAFCda24AA" #config("SESSION", default=None)
FORCESUB = "savebotvijay" #config("FORCESUB", default=None)
AUTH = "5409975736" #config("AUTH", default=None)
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
