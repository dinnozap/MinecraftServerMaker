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
	if yn == "Y" or yn == "y" or yn == y or yn == Y:
		cont = 0
	elif yn == "N" or yn == "n" or yn == N or yn == n:
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
	ServerBase=input("Please choose :\n (1)Spigot \n (2) Vanilla \n\n Enter 1 or 2  : ")
	if ServerBase == "1":
		clear()
		BoucleServer=False
		versionwant2=Ch_Spigot()
		clear()
		print
		print("We are downloading the server files, Please wait a few seconds .")
 
		download(versionwant2 , ServerName + "/" + ServerName+".jar")
		download("http://puu.sh/o8uA9/fbe7e61cc6.py",ServerName + "/" + "launch.py" )
		pathname = os.path.dirname(sys.argv[0])        
		pathact = os.path.abspath(pathname) + "\\"
		pathact = pathact + ServerName + '/'
		fichier = open(ServerName + "/" + "name.py", "w")
		fichier.write("ServerName = \""+ServerName+"\"")
		fichier.close()

		print("To start the server the server, launch the zero.py file in the folder " + ServerName)



	elif ServerBase == "2":
		clear()
		BoucleServer=False
		versionwant1=Ch_Vanilla()
		clear()
		print("We are downloading the server files, Please wait a few seconds .")
		download("http://puu.sh/o8uA9/fbe7e61cc6.py",ServerName + "/" + "launch.py" )
		download(versionwant1 , ServerName + "/" + ServerName+".jar")
		pathname = os.path.dirname(sys.argv[0])        
		pathact = os.path.abspath(pathname) + "\\"
		pathact = pathact + ServerName + '/'
		print("pathact")
		fichier = open(ServerName + "/" + "zero.py", "w")
		fichier.write("import os\n"+ "ServerName = "+"\""+ ServerName +"\""+ "\n" +"os.system(ServerName+ \".jar\")")
		fichier.close()
		print("To start the server the server, launch the zero.py file in the folder " + ServerName)
	else:
		BoucleServer = True
		clear()
		print("Please enter a correct value !!")
	











wait(2)
clear()
print("Now the program go start the server, press Ctrl + c for interupt the program !!")
wait(2)



############################