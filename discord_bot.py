import discord
import os
from keep_running import keep_running

client = discord.Client()
count = 5

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    global count
    if message.author == client.user:
        return
    elif count == 5:
        if message.author.id == 351810884781342720:
            await message.channel.send("Snake!")
            count -= 1
    elif count < 5 and count > 0:
        count -= 1
    elif count == 0:
        count += 5

keep_running()
client.run(os.getenv("token"))
