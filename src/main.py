import time
import datetime
from loguru import logger
from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest


logger.add(
    sink="log/main.log",
    format="[{time}][{level}]: {message} (line: {line})",
    level="DEBUG",
    rotation="1 MB",
    compression="zip"
)

logger.info("Author https://uw935.com/")

TEXT = "🕓 | Current local time: {time}"
API_ID = 0
API_HASH = ""

logger.info(f"API_ID: {API_ID}, API_HASH: {API_HASH}")

with TelegramClient(f".\\sessions\\{API_ID}", API_ID, API_HASH) as client:
    username = client.get_me().username
    logger.info(f"Successfully connected as @{username}")

    current_bio = client(GetFullUserRequest(username).full_user.about)
    logger.info(f"Current bio: {current_bio}")

    while True:
        today = datetime.datetime.today()

        client(UpdateProfileRequest(
            about=TEXT.replace("{time}", today.strftime("%H:%M:%S"))
        ))
        
        time.sleep(15)
