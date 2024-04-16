import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
# I want to be able to:
# - periodically check temperature/fan status and NOTIFY if necessary (ie. high temps)
# - Shutdown/reboot pi from the discord server by giving command to do so 
# - show active processes

load_dotenv()
TOKEN = os.getenv('MYPI_TOKEN')



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
# client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} connected to server MyPi')

    # start temp watch routine
    # notify user if temps rise above threshold and run fan until they cool below
    # if 5 minutes have passed with no drop to reasonable temps, schdule shutdown and notify user

@bot.command(name='checktemp')
async def checkTemp(context):

    # return current temp of pi (instantaneous, do not mess with fan)
    await context.send("Pi current temp: ???")

@bot.command(name='shutdown')
async def shutdown(context):

    # schedule the pi to shutdown, display shutdown message to user
    # end bot process (exit()) before shutdown
    await context.send("Scheduled pi to shutdown: ???")

@bot.command(name='reboot')
async def reboot(context):

    # schedule the pi to reboot, display reboot message to user
    await context.send("Scheduled pi to reboot: ???")

@bot.command(name='showactive')
async def showActive(context):

    # display the current active processes to the user
    await context.send("Active processes: ???")

bot.run(TOKEN)
