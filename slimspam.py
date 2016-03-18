import discord
import requests
import subprocess
import threading
import sys
import time

client = discord.Client()
inEmail = input("email: ")
inPassword = input("password: ")
if os.name == "nt":
	os.system("cls")
elif os.name == "posix":
	os.system('clear')
client.login(inEmail, inPassword)

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
