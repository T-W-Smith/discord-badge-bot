# bot.py
import discord
import random
import json
from discord.ext import commands

with open('config.json') as f:
    data = json.load(f)
    TOKEN = data["token"]
    #PREFIX = data["prefix"]

intent = discord.Intents.default() 
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix = "!", intents=intent)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='xol')
async def xol(ctx):
    xol_quotes = [
        'You shall drift.',
        'There is no Light here.',
        'You shall drown in the Deep.'
    ]

    response = random.choice(xol_quotes)
    await ctx.send(response)

# DONT USE THIS ITS SPAMMY
# @bot.event
# async def on_message(message):
#     if 'happy birthday' in message.content.lower():
#         await message.channel.send('Happy Birthday! 🎈🎉')

bot.run(TOKEN)
