# source env/bin/activate
from pyrogram import Client
from dotenv import load_dotenv
import tgcrypto
import os

load_dotenv()

CONFIG = {
    "telegram_api_id": int(os.getenv("TG_API_ID")),
    "telegram_hash": os.getenv("TG_API_HASH"),
}

app = Client("my_account",CONFIG["telegram_api_id"],CONFIG["telegram_hash"])

chat_id = "nytimes"

lst = []

filter = input("Enter keyword: ")

async def main():
    async with app:
        async for message in app.get_chat_history(chat_id):
            msg = str(message.text)
            if filter in msg:
                if msg not in lst:
                    lst.append(msg)

app.run(main())
lst.reverse()

with app:
    for i in lst:
        app.send_message("me", i)

print("done")