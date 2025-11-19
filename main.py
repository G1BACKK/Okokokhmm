from keepalive import keep_alive
keep_alive()


import os
from time import sleep
from pyrogram import Client

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
PHONE = os.environ["PHONE"]
CHANNEL = os.environ["CHANNEL"]

app = Client("session", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE)

def check_live():
    try:
        chat = app.get_chat(CHANNEL)
        if chat.video_chat:
            print("Live stream detected! Joining...")
            app.join_group_call(chat.id)
        else:
            print("No live stream now…")
    except Exception as e:
        print("Error:", e)

with app:
    while True:
        check_live()
        sleep(10)
