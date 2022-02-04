import os
import datetime
from nextcord.ext import commands
from dotenv import load_dotenv
from utils import your_ip

# laod all env variable
load_dotenv()

# prefix de commande du bot
bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print("Bot Ready")

# définir la command d'un bot avec le décorateur
@bot.command(name="clear")
async def delete(ctx, number:int=-1):
    if(number == -1.0):
        await ctx.channel.send(f"Vous avez oubliez de rentrer le nombre de messaque je dois supprimer")
        await ctx.channel.send(f"example: **>clear 2** ")
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
        
# find ip
@bot.command(name="myip")
async def time(ctx):
        result = your_ip.find_your_ip()
        await ctx.channel.send(f"Ton Ip => 💻 **{result}** 💻")


bot.run(os.environ.get('TOKEN'))
