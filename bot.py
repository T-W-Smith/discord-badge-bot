# bot.py
import discord
import random
import json
from discord.ext import commands
from discord.utils import get

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

@bot.command()
async def createeventrole(ctx):
    if get(ctx.guild.roles, name="Event Winner"):
        await ctx.send('Event Winner role has already been created')
    else:
        await ctx.guild.create_role(name='Event Winner')
        await ctx.send('Event Winner role created')

@bot.command(pass_context=True)
async def giveeventrole(ctx, user:discord.Member=None):
    if user == None:
        await ctx.send('Please specify a member')
    elif get(ctx.guild.roles, name='Event Winner'):
        role = get(ctx.guild.roles, name='Event Winner')
        await user.add_roles(role)
        await ctx.send(f'{user.name} has been give the {role.name} role!')
    else:
        await ctx.send('Event Winner role has not been created yet.')

@bot.command()
async def festivalwinner(ctx, user:discord.Member=None, emoji=None):
    if user.nick == None:
        nickname = f'{user.name} → {str(emoji)}'
        await user.edit(nick=nickname)
        await ctx.send(f'Nickname was changed for {user.mention}')
    else:
        nickname = f'{user.nick} → {str(emoji)}'
        await user.edit(nick=nickname)
        await ctx.send(f'Nickname was changed for {user.mention}')

@bot.command()
async def removewinner(ctx, user:discord.Member):
    nickname = user.nick
    newnick = nickname.split('→')[0]
    await user.edit(nick=newnick)
    await ctx.send(f'Nickname has been reset for {user.mention}')

#@bot.command(pass_context=True)
#async def giverole(ctx, user:discord.Member, rolename=None):
#    role = await ctx.guild.create_role(name=rolename, mentionable=True)
#    await user.add_roles(role)
#    await ctx.send(f"hey {ctx.author.name}, {user.name} has been given a role called: {role.name}")

bot.run(TOKEN)
