# -*- coding: utf-8 -*-
########################################
### 	Minecraft Server Maker 		####
### Create Your Own Minecraft Server ###
########################################
from commun import *

#Requests
import subprocess
import os, sys
import threading

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


#Create - Find ldink
ServerName = input("Please enter the name of your futur server : ")
if not os.path.exists(ServerName):
	os.mkdir(ServerName)
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

		download(versionwant1 , ServerName + "/" + ServerName+".jar")
		pathname = os.path.dirname(sys.argv[0])        
		pathact = os.path.abspath(pathname) + "\\"
		pathact = pathact + ServerName + '/'
		print("pathact")
		fichier = open(ServerName + "/" + "zero.py", "w")
		fichier.write("import subprocess\n"+ "ServerName = "+"\""+ ServerName +"\""+ "\n" +"subprocess.call([\'java\', \'-jar\',ServerName +  \"/\"+ ServerName+\'.jar\'])")
		fichier.close()
		sys.path.append(pathact)
		os.startfile(pathact + "zero.py") 

	elif ServerBase == "3":
		clear()
		BoucleServer=Falseo

	else:
		BoucleServer = True
		clear()
		print("Please enter a correct value !!")
	











wait(2)
clear()
print("Now the program go start the server, press Ctrl + c for interupt the program !!")
wait(2)



############################