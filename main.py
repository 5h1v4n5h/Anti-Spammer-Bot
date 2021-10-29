import discord
import os
from keep_alive import keep_alive
from urlchecker import urlchecker
import quotes
import urldetector

client = discord.Client()
my_secret = os.environ['Token']
urlcache = {}

@client.event
async def on_ready():
  print('We have been logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if len(urldetector.urldetector(message))>0:
    url_list = urldetector.urldetector(message)
    for i in url_list:
      #print(i)
      if i in urlcache:
        mess = urlcache[str(i)]
        mess = f'{message.author.mention}'+mess
        await message.reply(mess)
      elif i not in urlcache:
        mess = urlchecker(i)
        urlcache[i] = mess
        mess = f'{message.author.mention}'+mess 
        await message.reply(mess)
        #await message.channel.send(mess)
 
  if message.content.startswith('$inspire'):
    quot = quotes.inspire_quote()
    await message.channel.send(quot)
  elif message.content.startswith('$get quote'):
    await message.channel.send(quotes.get_quote())

keep_alive()
client.run(my_secret)