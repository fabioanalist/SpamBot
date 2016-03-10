import discord
import requests
import subprocess
import threading
import sys
import time
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    count = 100
    spamText = 'spam'
    uName = '9W9gz+DUk+uVQjhl/P7/JR8CsUD4o'
    targetUser = [m for m in client.get_all_members() if m.name == uName]
    for i in range(count):
        await client.send_message(targetUser[0], spamText)
        time.sleep(1)

client.run("metadatabot@gmail.com", "m3t4b0t")
