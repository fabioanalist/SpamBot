import discord
import requests
import subprocess
import threading
import sys
import os
import asyncio

client = discord.Client()


inEmail = input("email: ")
inPassword = input("password: ")
if os.name == "nt":
	os.system("cls")
elif os.name == "posix":
	os.system('clear')


helpMessage = ("+++++++++++++++++++++++++++++++++\n"
			   "+type 'help' to get help        +\n"
			   "+type 'exit' to exit the script +\n"
			   "type 'start' to start the attack+\n"
			   "+++++++++++++++++++++++++++++++++"
			   )

@client.event
async def on_ready():

	while 1:
		command = input(" # ")

		if command == "start":
			count = int(input("how many times: "))
			spamText = input("what do you want to send? ")
			uName = input("insert target name: ")
			targetUser = [m for m in client.get_all_members() if m.name == uName]
			print(targetUser)
			if count > 0 and count <= 1000:
				for i in range(count):
					await client.send_message(targetUser[0], spamText)
					await asyncio.sleep(1)

		if command == "exit":
			print("exiting script")
			client.logout()

		if command == "help":
			print(helpMessage)

	return;




client.run(inEmail, inPassword)
