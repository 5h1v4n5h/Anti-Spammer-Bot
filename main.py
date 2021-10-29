import discord
import os
from keep_alive import keep_alive
from urlchecker import urlchecker
import quotes
import urldetector
from replit import db

client = discord.Client() #creating basic client
my_secret = os.environ['Token'] #environment variable containing discord bot token
urlcache = {} #dictionary to store url:report used to prevent again and again  requesting same url using third party api


@client.event
async def on_ready():
  print('We have been logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
#------------------------------------------------------------
#Checking url in message and checking if its safe.-----------
#------------------------------------------------------------
  if len(urldetector.urldetector(message))>0:
    url_list = urldetector.urldetector(message)
    for i in url_list:
      if i in urlcache:
        mess = db[str(i)]
        mess = f'{message.author.mention}'+mess
        await message.reply(mess)
      elif i not in urlcache:
        mess = urlchecker(i)
        #urlcache[i] = mess
        if mess == None:
          mess = "The Url is invalid."
        db[i] = mess
        mess = f'{message.author.mention}'+mess 
        await message.reply(mess)
        #await message.channel.send(mess)
#------------------------------------------------------------
#Adding extra Commands for bot to make it Interactive.-------
#------------------------------------------------------------
  if message.content.startswith('$inspire'):
    quot = quotes.inspire_quote()
    await message.channel.send(quot)
  elif message.content.startswith('$get quote'):
    await message.channel.send(quotes.get_quote())

keep_alive()
client.run(my_secret)