from telethon import TelegramClient, events
from termcolor import cprint
import asyncio

from src.main import client
from src.config import Config
from src.service.message import generate_messge
from src.service import DataBase
db = DataBase(Config.db_name)


print("✅ Success - user ")


@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.is_private:
        if len(await db.UserFind(event.chat_id)) == 0:
            await event.respond(await generate_messge())
            await db.UserAdd(event.chat_id)