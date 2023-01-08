from telethon import TelegramClient, events
from termcolor import cprint
import asyncio

from src.config import Config
from src.service import DataBase
db = DataBase(Config.db_name)


#initialize user agent
client = TelegramClient(Config.session_location, Config.api_id, Config.api_hash)

#Main function
async def main():

    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    cprint('🔱 The user bot was written by a genius - AlexZai007', "cyan")
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    from handlers import client

    try:

        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        cprint("✅ Success - The user bot has established a connection with the telegram server", "green")
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        await client.start()
        await client.run_until_disconnected()
    finally:
        cprint("❌Stopped - the user bot stopped communicating with the server", "red")


#Starter
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        cprint("❌Stopped - The bot has been stopped by the user", "red")





