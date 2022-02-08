import os
import datetime
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from utils import your_ip, keep_alive, button_usefull
from utils.music import Music

# laod all env variable
load_dotenv()

# prefix de commande du bot
bot = commands.Bot(command_prefix=">",description="Maxvyr personnal bot")

@bot.event
async def on_ready():
    print('✅\n{0.user.name} is Ready \n✅'.format(bot))
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name="Some Boring thing"))

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
    elif  num >= 1 :
     gif = "https://i.imgur.com/nbhmInn.png"   
    else :
        gif = "https://c.tenor.com/VUQaWMnKtgAAAAAd/no-let-me-think.gif"

    await ctx.message.add_reaction('✅')
    await ctx.channel.send(gif)
    
@bot.command(name="link")
async def link_usefull(ctx):
    view = button_usefull.button_link_manhwa()
    await ctx.send("Yes Master!", view=view)

    

# keep_alive.keep_alive()
bot.add_cog(Music(bot))

bot.run(os.environ.get('TOKEN'))
