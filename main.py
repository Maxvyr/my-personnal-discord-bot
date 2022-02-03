from difflib import restore
from email import message
import discord
import os
import datetime
from discord.ext import commands
from dotenv import load_dotenv

# laod all env variable
load_dotenv()

# prefix de commande du bot
bot = commands.Bot(command_prefix="!")

default_intents = discord.Intents.default()
default_intents.members = True

client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")
    
@client.event
async def on_member_join(member):
    channel_arrive = client.get_channel(696992636485238787)
    channel_arrive.send(f"Bienvenue à {member.display_name} ! ")
    print(f"L'utilisateur {member.display_name} à rejoint")

@bot.event
async def on_ready():
    print("Bot Ready")

# définir la command d'un bot avec le décorateur
@bot.command(name="del")
async def delete(ctx, number:int=-1):
    if(number == -1.0):
        await ctx.channel.send(f"Vous avez oubliez de rentrer le nombre de messaque je dois supprimer")
        await ctx.channel.send(f"example: **!del 2** ")
        await ctx.channel.send(f"Si vous voulez **supprimer** les **2 messages précédents**")
    else:
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    
# delay message
@bot.command(name="remind")
async def time(ctx, minutes:float = -1.0):
    if(minutes == -1.0):
        await ctx.channel.send(f"Vous avez oubliez de rentrer la valeur en minutes de quand vous souhaitez je vous rappel se message")
    else:
        now = datetime.datetime.now()
        delta = datetime.timedelta(minutes=minutes) 
        result = now + delta
        await delete(ctx, 1)
        await ctx.channel.send(f"Date => {now} & {result}")


bot.run(os.environ.get('TOKEN'))
