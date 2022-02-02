import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run("OTM4MTgxNTM0NjM1MTU5NjQz.YfmjpA.YpclhC4bqSlkCaLOM9rsBT5q9OQ")
