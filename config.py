import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8294380111:AAE-OxqUwNSw5jqBNp3OfGGd7Ptx665Kz8s")
API_ID = int(os.environ.get("API_ID", "30506021"))
API_HASH = os.environ.get("API_HASH", "3c2a9654081a4c96f441f6ff0d633b58")


OWNER_ID = int(os.environ.get("OWNER_ID", "5533100886"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Anime11tamil:Anime11tamil_4321@cluster0.rmp2lb3.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Anime11tamil")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001945519823"))

FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1001945519823"))

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1001945519823"))

FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0"))

FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))

START_PIC = os.environ.get("START_PIC", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6W7h6ni2-yfPUyF2TY_t22jf9R2oD5995479FrcbM3OZyJ2TES5O4FWIwVxuaAO7UfL-OfHnRvYyR_WP0bzkNI_3tjWJ5sWNEOXMzuiDozRxl0qQBSHStXK0zUcvEvht12AhCPUARKYCXwJYXXFn0aUoYxrvnQSqBtgYlhejIHGtguij0kkoospg2tg/s1080/one%20piece%20%5B74CCC6F%5D.png")
F_PIC = os.environ.get("FORCE_PIC", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6W7h6ni2-yfPUyF2TY_t22jf9R2oD5995479FrcbM3OZyJ2TES5O4FWIwVxuaAO7UfL-OfHnRvYyR_WP0bzkNI_3tjWJ5sWNEOXMzuiDozRxl0qQBSHStXK0zUcvEvht12AhCPUARKYCXwJYXXFn0aUoYxrvnQSqBtgYlhejIHGtguij0kkoospg2tg/s1080/one%20piece%20%5B74CCC6F%5D.png")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8050")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[5533100886 ,1882587557]
    for x in (os.environ.get("ADMINS", "5533100886").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Sry You can't Able to Message me !\n\n» My Owner 👉 "

START_MSG = os.environ.get("START_MESSAGE", "<b>Hi {first} Friend I am a Advance File Store bot 😈 \n\n I was created by 👉@Anime_lockers_bot </b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} You must join the given channels ..\n\n 𝐒𝐨 please join and  “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")




ADMINS.append(OWNER_ID)
ADMINS.append(5533100886)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href=''>[AW] File store bot 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/anime11tamil'>Anime_lockers_bot</a>
<b>🛡️ :</b> <a href='https://t.me/anime11tamil'>Anime_lockers_bot</a>
    
<b>😈 Bot Made By :</b> @Obito_205"""


# anime11tamil 
# Don't Remove Credit!!!
# Telegram Channel @Obito_205
# Developer @Obito_205
