# bot.py
import discord
import random
import json
from discord.ext import commands
from discord.utils import get

with open('config.json') as f:
    data = json.load(f)
    TOKEN = data["token"]
    PREFIX = data["prefix"]

intent = discord.Intents.default() 
intent.members = True
intent.message_content = True
bot = commands.Bot(PREFIX, intents=intent)

# Change only the no_category default string
bot.help_command = commands.DefaultHelpCommand(
    no_category = 'Commands',
)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(
    brief='XOL', 
    description='DROWN')
async def xol(ctx):
    xol_quotes = [
        'You... shall... drift...',
        'There.. is.. no.. Light.. here...',
        'You.. shall.. drown.. in the.. Deep...'
    ]
    response = random.choice(xol_quotes)
    await ctx.send(response)
    await ctx.message.delete()
    

@bot.command(
    brief='Creates the Event Role', 
    description='Creates the Event Role for the event winners.')
async def createeventrole(ctx):
    if get(ctx.guild.roles, name="Event Winner"):
        await ctx.send('Event Winner role has already been created')
    else:
        await ctx.guild.create_role(name='Event Winner')
        await ctx.send('Event Winner role created')
    await ctx.message.delete()


@bot.command(
    brief='Adds FotL winner', 
    description='Adds the mentioned member to the Event Winner role and gives them a special emoji: 🎃.')
async def addfestivalwinner(ctx, user:discord.Member=None):
    if user == None:
        await ctx.send('Please specify a member.')
    elif get(ctx.guild.roles, name='Event Winner'):
        nickname = f'{user.name} → 🎃'
        await user.edit(nick=nickname)
        role = get(ctx.guild.roles, name='Event Winner')
        await user.add_roles(role)
        await ctx.send(f'Congratulations {user.mention} on winning the Cosmic Templars Festival of the Lost community event!')
    else:
        await ctx.send('Event Winner role has not been created yet.')
    await ctx.message.delete()

@bot.command(
    brief='Removes FotL winner', 
    description='Removes the Festival of the Lost winner from the Event Winner role and removes their special emoji: 🎃.')
async def removefestivalwinner(ctx):
    role = get(ctx.guild.roles, name='Event Winner')
    if role:
        for m in role.members:
            if '🎃' in m.nick:
                newnick = m.nick.split('→')[0]
                await m.edit(nick=newnick)
                role = get(ctx.guild.roles, name='Event Winner')
                await m.remove_roles(role)
                await ctx.send('A new Festival of the Lost winner shall be crowned')
    else:
        await ctx.send('Event Winner role has not been created yet.')
    await ctx.message.delete()


@bot.command(
    brief='Adds Dawning winner', 
    description='Adds the mentioned member to the Event Winner role and gives them a special emoji: ⛄.')
async def adddawningwinner(ctx, user:discord.Member=None):
    if user == None:
        await ctx.send('Please specify a member.')
    elif get(ctx.guild.roles, name='Event Winner'):
        nickname = f'{user.name} → ⛄'
        await user.edit(nick=nickname)
        role = get(ctx.guild.roles, name='Event Winner')
        await user.add_roles(role)
        await ctx.send(f'Congratulations {user.mention} on winning the Cosmic Templars Dawning community event!')
    else:
        await ctx.send('Event Winner role has not been created yet.')
    await ctx.message.delete()

@bot.command(
    brief='Removes Dawning winner', 
    description='Removes the Festival of the Lost winner from the Event Winner role and removes their special emoji: ⛄.')
async def removedawningwinner(ctx):
    role = get(ctx.guild.roles, name='Event Winner')
    if role:
        for m in role.members:
            if '⛄' in m.nick:
                newnick = m.nick.split('→')[0]
                await m.edit(nick=newnick)
                role = get(ctx.guild.roles, name='Event Winner')
                await m.remove_roles(role)
                await ctx.send('A new Dawning winner shall be crowned')
    else:
        await ctx.send('Event Winner role has not been created yet.')
        await ctx.message.delete()


@bot.command(
    brief='Adds Guardian Games winner', 
    description='Adds the mentioned member to the Event Winner role and gives them a special emoji: 🏅.')
async def addguardianwinner(ctx, user:discord.Member=None):
    if user == None:
        await ctx.send('Please specify a member.')
    elif get(ctx.guild.roles, name='Event Winner'):
        nickname = f'{user.name} → 🏅'
        await user.edit(nick=nickname)
        role = get(ctx.guild.roles, name='Event Winner')
        await user.add_roles(role)
        await ctx.send(f'Congratulations {user.mention} on winning the Cosmic Templars Guardian Games community event!')
    else:
        await ctx.send('Event Winner role has not been created yet.')
    await ctx.message.delete()

@bot.command(
    brief='Removes Guardian Games winner', 
    description='Removes the Festival of the Lost winner from the Event Winner role and removes their special emoji: 🏅.')
async def removeguardianwinner(ctx):
    role = get(ctx.guild.roles, name='Event Winner')
    if role:
        for m in role.members:
            if '🏅' in m.nick:
                newnick = m.nick.split('→')[0]
                await m.edit(nick=newnick)
                role = get(ctx.guild.roles, name='Event Winner')
                await m.remove_roles(role)
                await ctx.send('A new Guardian Games winner shall be crowned')
    else:
        await ctx.send('Event Winner role has not been created yet.')
    await ctx.message.delete()


@bot.command(
    brief='Adds Summer Solstice winner', 
    description='Adds the mentioned member to the Event Winner role and gives them a special emoji: 🌞.')
async def addsummerwinner(ctx, user:discord.Member=None):
    if user == None:
        await ctx.send('Please specify a member.')
    elif get(ctx.guild.roles, name='Event Winner'):
        nickname = f'{user.name} → 🌞'
        await user.edit(nick=nickname)
        role = get(ctx.guild.roles, name='Event Winner')
        await user.add_roles(role)
        await ctx.send(f'Congratulations {user.mention} on winning the Cosmic Templars Summer Solstice community event!')
    else:
        await ctx.send('Event Winner role has not been created yet.')
    await ctx.message.delete()

@bot.command(
    brief='Removes Summer Solstice winner', 
    description='Removes the Festival of the Lost winner from the Event Winner role and removes their special emoji: 🌞.')
async def removesummerwinner(ctx):
    role = get(ctx.guild.roles, name='Event Winner')
    if role:
        for m in role.members:
            if '🌞' in m.nick:
                newnick = m.nick.split('→')[0]
                await m.edit(nick=newnick)
                role = get(ctx.guild.roles, name='Event Winner')
                await m.remove_roles(role)
                await ctx.send('A new Summer Solstice winner shall be crowned')
    else:
        await ctx.send('Event Winner role has not been created yet.')
    await ctx.message.delete()


bot.run(TOKEN)
