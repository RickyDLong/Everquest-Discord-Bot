import discord
from dotenv import load_dotenv
import os
import Auction

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('We are online')

@client.event
async def message(message):
    # if message is from the bot, ignore it
    if message.author == client.user:
        return
    # if message comes from command in discord
    if message.content.startswith('$auctions'):
        await message.channel.send("`" + Auction.main() + "`")

    elif message.content.startswith('$help'):
        await message.channel.send("Under Construction")

client.run(os.getenv("TOKEN"))
