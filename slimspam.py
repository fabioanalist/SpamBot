import discord
import requests
import subprocess
import threading
import sys
import time

client = discord.Client()
client.login('metadatabot@gmail.com', 'm3t4b0t')

@client.event
def on_ready():
    count = 100
    spamText = 'spam'
    uName = 'AolDhajoly'
    targetUser = [m for m in client.get_all_members() if m.name == uName]
    for i in range(count):
        client.send_message(targetUser[0], spamText)
        time.sleep(0.7)

client.run()
