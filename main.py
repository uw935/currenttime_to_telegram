from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
import datetime, time

print("Author: https://github.com/uw935/ \nTelegram: @uw935.\n")
print("Please, use CTRL+C to exit\n\n")

API_ID   = int(input("Enter you API ID: "))
API_HASH = str(input("Enter you API HASH: "))

with TelegramClient('session', API_ID, API_HASH) as client:
	bionow = str(client(GetFullUserRequest(client.get_me().username)).about)

	print(f"\nSuccessful connected as {client.get_me().username}")

	while True:
		try:
			today = datetime.datetime.today()

			client(UpdateProfileRequest(about = "🕓 | Current local time: " + today.strftime("%H:%M:%S")))
			time.sleep(15)

		except:
			client(UpdateProfileRequest(about = bionow))
			client.disconnect()



