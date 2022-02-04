import os
import datetime
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from utils import your_ip, keep_alive

# laod all env variable
load_dotenv()

# prefix de commande du bot
bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print("Bot Ready")
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Some Boring thing"))

# définir la command d'un bot avec le décorateur
@bot.command(name="del")
async def delete(ctx, number:int=-1):
    if number == -1.0 :
        await ctx.channel.send(f"Vous avez oubliez de rentrer le nombre de messaque je dois supprimer")
        await ctx.channel.send(f"example: **>del 2** ")
        await ctx.channel.send(f"Si vous voulez **supprimer** les **2 messages précédents**")
    else:
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    
# delay message
@bot.command(name="remind")
async def time(ctx, minutes:float = -1.0):
    if minutes == -1.0 :
        await ctx.channel.send(f"Vous avez oubliez de rentrer la valeur en minutes de quand vous souhaitez je vous rappel se message")
    else:
        now = datetime.datetime.now()
        delta = datetime.timedelta(minutes=minutes) 
        result = now + delta
        await delete(ctx, 1)
        await ctx.channel.send(f"Date => {now} & {result}")
        
# find ip
@bot.command(name="myip")
async def my_ip(ctx):
        result = your_ip.find_your_ip()
        await ctx.channel.send(f"Ton Ip => 💻 **{result}** 💻")
               
# troll
@bot.command(name="img")
async def troll(ctx, num=-1):
    gif = ""
    if num == -1 :
     gif = "https://c.tenor.com/VUQaWMnKtgAAAAAd/no-let-me-think.gif"   
    elif  num >= 2 :
     gif = "https://i.imgur.com/nbhmInn.png"   
    else :
        gif = "https://c.tenor.com/VUQaWMnKtgAAAAAd/no-let-me-think.gif"

    # await delete(ctx, number=1)
    await ctx.channel.send(gif)
    

keep_alive.keep_alive()

bot.run(os.environ.get('TOKEN'))
