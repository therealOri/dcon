# Code made by Ori#6338 | <-- DO NOT REMOVE PLS. THIS IS MY CREDITS FOR CODE BEING MADE FOR FREE.

import discord
import os
import random
from dotenv import load_dotenv # This is for the .env file you will put your token in.
import colorama
from colorama import Fore
from discord.ext import commands, tasks
import asyncio
import datetime

load_dotenv() # This loads the .env file
TOKEN = os.getenv("TOKEN") # This gets the token veriable in the .env file. | makes the word TOKEN be that actual bot token you copy and pasted into the .env file.

# Client Setup.
BOT_Prefix=("a.") # Sets your prefix as whatever you want.
client = commands.Bot(command_prefix=BOT_Prefix)
client.remove_command("help") # The help command below won't work unless this is here, as python3 thinks there is already a help command.

botver = "BOT_NAME v1.0" # This is just for fancy embed footers to display what the version the bot is.


# Lets you know when the bot is online and working in the cmd window/terminal.
@client.event
async def on_ready():
    print(Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + f" connection established and logged in as: {client.user.name} with ID: {client.user.id}")



# Gives you the bots commands.
# colour=0x941db4 this is a hex color value. it can be changed to whatever. 0x stays and then anything you want after. example: 0x00ffff
@client.command()
async def help(ctx):
    await ctx.message.delete()
    
    # If you change the bots prefix, make sure to update the following text with the correct prefix/new prefix.
    helpembed = discord.Embed(title="Commands", description=('A helpful menu for all the commands this bot can do! | Made by Ori#6338'), colour=0x941db4, timestamp=datetime.datetime.utcnow())
    helpembed.set_thumbnail(url='https://discord.com/assets/3c6ccb83716d1e4fb91d3082f6b21d77.png') # This can be changed to your discord bots icon.
    helpembed.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", value='\u200b', inline=False)
    helpembed.add_field(name="a.gicon", value = "Starts the timer for guild icon changing.")
    helpembed.add_field(name="a.gstop", value = "Stops the timer.", inline=False)
    helpembed.add_field(name="a.ping", value = "Ping Pong. (Pings the bot)", inline=False)
    helpembed.add_field(name="\u200b", value='▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬', inline=False)
    helpembed.set_footer(text=f"{botver} | code made by Ori#6338", icon_url='https://cdn.discordapp.com/attachments/850592305420697620/850595192641683476/orio.png') #Credits for code being free.
    await ctx.send(embed=helpembed)



# A simple command to see if the bot is responsive and working.
@client.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"My connection speed is {round(client.latency * 1000)}ms", color=discord.Color.random(), timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f"{botver} | code made by Ori#6338", icon_url='https://cdn.discordapp.com/attachments/850592305420697620/850595192641683476/orio.png') #Credits for code being free.
    await ctx.send(embed=embed)


# This is what keeps the loop going and running.
@tasks.loop()
async def timer():
    while True:
        await asyncio.sleep(86400) # 86400s = 24hrs

        # Since you are very likely using Windows, use the windows path format | C:\Useres\YOUR_NAME\Desktop\niall\images\ <-- This kind of thing. (make it lead to wherever you keep your images/icons)
        path = "/home/ori/Desktop/niall/images/" # This is the path to the images folder where you will keep the images you want to be used for guild icons.
        image = random.choice(os.listdir(path)) # This sudo randomly selects one.

        # This opens the "randomly" selected image from above and reads the data/bytes.
        with open(f'{path}/{image}', 'rb') as f:
            icon = f.read()
        
        # This gets the guilds ID this bot is in and edits the guild icon.
        guild = client.get_guild(GUILD_ID_HERE)
        await guild.edit(icon=icon)


# Starts timer and icon changing
@client.command()
async def gicon(ctx): #"gicon" is the name of the command that will be used. This can be changed to whatever. Same goes for any of the other commands. Don't change the name for the timer.
    await ctx.message.delete()
    if not timer.is_running(): # If the timer isn't started, it starts the timer.
        timer.start()
        print('Timer started!')
    else: # If the timer/this command has already been run, say that the timer has already been started.
        print('Timer already started')

#Stops the timer
@client.command()
async def gstop(ctx):
    await ctx.message.delete()

    timer.cancel()
    print("Timer Stopped for guild icon chnage!")

# Tells discord to use the token you have provided in the .env file.
client.run(TOKEN)
