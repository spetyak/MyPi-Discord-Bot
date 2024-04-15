import os
import discord
from dotenv import load_dotenv
# I want to be able to:
# - periodically check temperature/fan status and NOTIFY if necessary (ie. high temps)
# - Shutdown/reboot pi from the discord server by giving command to do so 
# - show active processes

load_dotenv()
TOKEN = os.getenv('MYPI_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} connected to server MyPi')

client.run(TOKEN)
