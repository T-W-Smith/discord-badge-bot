# bot.py
import discord
import random
import json
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions

with open('config.json') as f:
    data = json.load(f)
    TOKEN = data["token"]
    PREFIX = data["prefix"]

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(PREFIX, intents=intent)


bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
@has_permissions(kick_members=True)
async def help(ctx):
    help_message = """
```adddawningwinner = Adds Dawning winner
addfestivalwinner = Adds FotL winner
addguardianwinner = Adds Guardian Games winner
addsummerwinner = Adds Summer Solstice winner
createeventrole = Creates the Event Role
help = Shows this message
removedawningwinner = Removes Dawning winner
removefestivalwinner = Removes FotL winner
removeguardianwinner = Removes Guardian Games winner
removesummerwinner = Removes Summer Solstice winner
xol = XOL```"""
    await ctx.send(help_message)


@bot.command(
    brief='XOL', 
    description='DROWN')
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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
@has_permissions(kick_members=True)
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