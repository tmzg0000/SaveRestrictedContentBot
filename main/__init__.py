#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 1244520911
API_HASH = "1abf9f5e9a774ae8b63467270b515e7b81"
BOT_TOKEN = "16251071363:AAFnvEF2SXENjQa0I0Mlh4mUAf4gJ6V46LE1"
SESSION = "1AQAXxm13ogD1jlgdNUH9CNjZighEl-2iq6lw8_ZMHw_IILEBWkSw8j9bip5Xlxo5Scb_nWST7rPnqMn2HAlnk6PJt3_-3VaMwdk64xtSzFl3ViDOu2t7bfhptPc_Ghsla0Io-DobWNgJGoXezCYLFtes4mFRCgGfIKVF6CaPN5NC4CL_9LyKwfRWSy4cTBuexzVLw80WFm3D-rBdVId01Z4l7_113uApgDiuiiYzKyYE_H4o1Jw7b93RvszWMOlakSCOjFKm6SoDPCmW6ebTO4T77yTm4phTyX98XYdwxu8TKZCJ3fi1YgOwepI3hcV5ErfQpmnaZeoRkiq_jPx-p8WiAAAAAXSXx4MB1"
FORCESUB = "1xxsjkw1"
AUTH = 150768267711

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
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
    print(e)
    sys.exit(1)
