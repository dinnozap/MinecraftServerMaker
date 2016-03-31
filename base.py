# -*- coding: utf-8 -*-
########################################
### 	Minecraft Server Maker 		####
### Create Your Own Minecraft Server ###
########################################
from commun import *

#Requests
import subprocess
import os


clear()
yn = input("Do you really want to create your Minecraft Server ? Y/N     :")


cont = 1
while cont:
	if yn == "Y" or yn == "y":
		cont = 0
	elif yn == "N" or yn == "n":
		exit(0)
	else:
		print("Wait one second...")
		wait(1)
		print("Please enter a correct value:")
		yn = input("Do you really want to create your Minecraft Server ? Y/N")


#Create - Find link
ServerName = input("Please enter the name of your futur server : ")
BoucleServer=True

while BoucleServer:
	ServerBase=input("Please choos :\n (1) CraftBukkit \n (2) Vanilla \n (3) Spigot\n\n Enter 1 or 2 or 3 : ")
	if ServerBase == "1":
		clear()
		BoucleServer=False	

	elif ServerBase == "2":
		clear()
		BoucleServer=False
		versionwant1=Ch_Vanilla()
		clear()
		print("We are downloading the server files, Please wait a few seconds .")

		download(versionwant1 , ServerName+".jar")
		subprocess.run(['java', '-jar', 'serveur/' + ServerName + '.jar'])

	elif ServerBase == "3":
		clear()
		BoucleServer=False

	else:
		BoucleServer = True
		clear()
		print("Please enter a correct value !!")
	











wait(2)
clear()
print("Now the program go start the server, press Ctrl + c for interupt the program !!")
wait(2)



############################