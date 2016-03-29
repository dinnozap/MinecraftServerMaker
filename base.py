# -*- coding: utf-8 -*-
########################################
### 	Minecraft Server Maker 		####
### Create Your Own Minecraft Server ###
########################################
from commun import *
import requests
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
serv=input("Please enter the version of your futur server (1.x or 1.x.x) :")
chemin=input("Now enter the folder of your server ( ex: /home/mcm/serv/ or C:/Users/mcm/serv")
serv1 = float(serv)
versionwant=server(serv)
if serv1 < 1.4:
        print("Sorry but the versions under 1.4 are not in charge by MCSM")
elif serv1 >= 1.4:
	ydown=input("The program go download the server jar files . Do you want to continue ? Y/N :")
	cont = 1
	while cont:
		if ydown == "Y" or ydown =="y":
			pass
			cont = 0
		elif ydown == "N" or ydown == "n":
			exit(0)
		else:
			print("Wait one second...")
			wait(1)
			print("Please enter a correct value:")
			ydown = input("The program go download the server jar files . Do you want to continue ? Y/N :")

print("We are downloading the server files, Please wait a few seconds .")
fileName = chemin +'serv.jar'
req = requests.get(versionwant)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
print("The download is finish !")
wait(2)
clear()
servstart =input("Now you need to start the server, do you want to start the server ? Y/N :")

############################