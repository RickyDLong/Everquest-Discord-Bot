import discord
from dotenv import load_dotenv
import os

import Auction

load_dotenv()
client = discord.Client()
TOKEN = os.getenv("TOKEN")
@client.event()
async def onReady():
    print("EQ Bot Online")

@client.event()
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        await message.channel.send("Under Construction")

@client.event()
async def find_auction(message):
    if message.author == client.user:
        return
    clientItem = ""
    if message.content.startswith('$watch' + clientItem):
        if clientItem in Auction.findItems():




client.run(TOKEN)
