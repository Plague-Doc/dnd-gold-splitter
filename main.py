from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# LOAD TOKEN FROM ENV
load_dotenv()
TOKEN: Final[str] = str(os.getenv('DISCORD_TOKEN'))

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents = intents)

# MESSAGE FUNCTIONS
async def send_message(message: Message, user_messsage: str) -> None:
    if not user_messsage:
        print("Empty message, fucked up intents")
        return
    
    if user_messsage.split()[0] != "!split" and user_messsage.split()[0] != "/split":
        return
    
    try:
        response: str = get_response(user_messsage)
        await message.channel.send(response)
    except Exception as e:
        print(f"[DEBUG] {e}")

# BOT STARTUP
@client.event
async def on_ready() -> None:
    print(f"{client.user} is running.")

# INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    user: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {user}: {user_message}")
    await send_message(message, user_message)

# MAIN ENTRYPOINT
if __name__ == '__main__':
    client.run(token=TOKEN)