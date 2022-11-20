import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  channel = str(message.channel.name)
  username = str(message.author).split("#")[0]
  if channel == "music-board":
    if message.author == client.user:
      return
       
    if message.content.startswith("https://youtu.be/"):
      text = str(message.content)
      song = "https://play.laibaht.ovh/watch?v="+text[17:]
      await message.channel.send(f"----------------------------------- \n ไอ{username} มันขอเพลง")
      await message.channel.send(song)
      await message.delete()
        
    if message.content.startswith("https://www.youtube.com/watch?v="):
      text = str(message.content)
      song = "https://play.laibaht.ovh/watch?v="+text[32:]
      await message.channel.send(f"----------------------------------- \n ไอ{username} มันขอเพลง")
      await message.channel.send(song)
      await message.delete()
          
  else:
    return


client.run(TOKEN)