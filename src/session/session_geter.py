import asyncio
from pyrogram import Client


"""
applications for getting a telegram session. After the correct operation of the program. 
The session will be saved under the name "anon" and will be sent to saved telegram messages.
"""

async def main():
    api_id = int(input("API ID: "))
    api_hash = input("API HASH: ")
    async with Client("anon", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**Your session by alexzai007 (don't give it to anyone)**:\n\n"
            f"`{await app.export_session_string()}`"
        )
        print(
            "Done, your Pyrogram session string has been sent to "
            "Saved Messages of your Telegram account!"
        )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())