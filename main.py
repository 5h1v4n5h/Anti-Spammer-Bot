import discord
import os
from keep_alive import keep_alive
from urlchecker import urlchecker
import attachment_virusscan
import quotes
import urldetector
import Antispammer

client = discord.Client()
my_secret = os.environ['Token']
urlcache = {}


@client.event
async def on_ready():
    print('We have been logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
    member = message.author
    if message.author == client.user:
        return
    if len(urldetector.urldetector(message)) > 0:
        url_list = urldetector.urldetector(message)
        for i in url_list:
            if i in urlcache:
                mess = urlcache[str(i)]
                mess = f'{message.author.mention}' + mess
                await message.reply(mess)
            elif i not in urlcache:
                mess = urlchecker(i)
                if mess != None:
                    urlcache[i] = mess
                    mess = f'{message.author.mention}' + mess
                    await message.reply(mess)
    if message.content.startswith('$inspire'):
        quot = quotes.inspire_quote()
        await message.channel.send(quot)
    elif message.content.startswith('$get quote'):
        await message.channel.send(quotes.get_quote())
    else:
        lst = []
        lst = [
            msg.content for msg in await message.channel.history().flatten()
            if msg.author == member
        ]
        lst1 = Antispammer.spam_check(list(lst))
        if len(lst1) > 0:
            if message.content in lst1 :
                await message.delete()
                mess = f'{message.author.mention}' + "Don\'t Spam \n Your spammed message will be deleted."
                await message.channel.send(mess)

    if message.attachments:
        image_types = ["png", "jpeg", "gif", "jpg"]
        for attachment in message.attachments:
            download_path = "tempdownload/" + attachment.filename
            if any(attachment.filename.lower().endswith(image)
                   for image in image_types):
                await attachment.save("tempdownload/" + attachment.filename)
            else:
                await attachment.save("tempdownload/" + attachment.filename)
            mess = attachment_virusscan.file_scanner(download_path)
            if mess != None:
                mess = f'{message.author.mention}' + mess
                await message.reply(mess)


keep_alive()
client.run(my_secret)
