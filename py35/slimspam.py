import discord
import requests
import subprocess
import threading
import sys
import time
import asyncio

client = discord.Client()


inEmail = input("email: ")
inPassword = input("password: ")
if os.name == "nt":
	os.system("cls")
elif os.name == "posix":
	os.system('clear')


@client.event
async def on_ready():
    count = 100
    spamText = 'spam'
    uName = '9W9gz+DUk+uVQjhl/P7/JR8CsUD4o'
    targetUser = [m for m in client.get_all_members() if m.name == uName]
    for i in range(count):
        await client.send_message(targetUser[0], spamText)
        await asyncio.sleep(1)

client.run(inEmail, inPassword)
