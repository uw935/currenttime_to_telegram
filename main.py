from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import config, datetime, time


print("Hi! This is TELEGRAM APP - TIME. If you have not entered the data, then enter your data in the config.py file for further work. If you have any questions or error - write me. \n \n Author: https://github.com/UW935\n TELEGRAM: @uw935")

#переменные
session_name = 'session'
ApiId = config.api_id
ApiHash = config.api_hash
a = 5

while a < 50:
	with TelegramClient(session_name, config.api_id, config.api_hash) as client:
		today = datetime.datetime.today()
		profile_bio = "🕓| Current time: " + today.strftime("%H:%M:%S")
		client(UpdateProfileRequest(about=profile_bio))
		time.sleep(10)

#говнокод))