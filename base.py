
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

def main():
	yn = input('Do you really want to create your Minecraft Server ? Y/N     :')


	cont = 1
	while cont:
		if yn == 'Y' or yn == 'y':
			cont = 0
		elif yn == 'n' or yn == 'N':
			exit(0)
		else:
			print('Wait one second...')
			wait(1)
			print('Please enter a correct value:')
			yn = input('Do you really want to create your Minecraft Server ? Y/N : ')


	#Create - Find ldink
	ServerName = input('Please enter the name of your futur server : ')

	pathname = os.path.dirname(sys.argv[0])       
	pathact = os.path.abspath(pathname) + '/'
	pathact = pathact + ServerName + '/'
	clear()
	pathserver = input('\n\nDo you want to create your server in this path :'+ pathact +' \nY/N : ')

	contpathserv = True
	pathtrue = True

	clear()
	def pathcourrant():
		BoucleServer = True
		while BoucleServer:
			ServerBase=input('Please choose :\n (1) Spigot \n (2) Vanilla \n\n Enter 1 or 2  : ')
			if ServerBase == '1':
				clear()
				BoucleServer=False
				versionwant2=Ch_Spigot()
				clear()
				print
				print('We are downloading the server files, Please wait a few seconds .')
		 
				download(versionwant2[0] , ServerName + '/' + ServerName+'.jar')
				clear()
				download('https://raw.githubusercontent.com/dinnozap/MinecraftServerMaker/master/launch.py',ServerName + '/' + 'launch.py')
				fichier = open(ServerName + '/' + 'name.info', 'w')
				fichier.write(ServerName + '\n' + ServerBase + '\n'+ versionwant2[1])
				fichier.close()




			elif ServerBase == '2':
				clear()
				BoucleServer=False
				versionwant1=Ch_Vanilla()
				clear()
				print('We are downloading the server files, Please wait a few seconds .')
				download('http://92.222.88.229/msm/launch.py',ServerName + '/' + 'launch.py' )
				clear()
				download(versionwant1[0] , ServerName + '/' + ServerName+'.jar')
				print('pathact')
				fichier = open(ServerName + '/' + 'name.info', 'w')
				fichier.write(ServerName +'\n'+ ServerBase +'\n'+ versionwant1[1])
				fichier.close()
				print('To start the server the server, launch the zero.py file in the folder ' + ServerName)
			else:
				BoucleServer = True
				clear()
				print('Please enter a correct value !!')

			wait(2)
			clear()
			print('To start the server the server, launch the launch.py file in the folder of your server :' + ServerName + "\n \n \n ")
			print('Now the program go start the server, press Ctrl + c for interupt the program !!')
			wait(5)
			clear()
			exit(0)
			
	def pathchoose():
		BoucleServer = True
		while BoucleServer:
			ServerBase=input('Please choose :\n (1)Spigot \n (2) Vanilla \n\n Enter 1 or 2  : ')
			if ServerBase == '1':
				clear()
				BoucleServer=False
				versionwant2=Ch_Spigot()
				clear()
				print
				print('We are downloading the server files, Please wait a few seconds .')
		 
				download(versionwant2[0] , pathact  + ServerName+'.jar')
				download('http://puu.sh/ocZCU/a64fb806f8.py',pathact  + 'launch.py')
				fichier = open(pathact + '/' + 'name.info', 'w')
				fichier.write(ServerName + '\n' + ServerBase + '\n'+ versionwant2[1])
				fichier.close()

				print('To start the server the server, launch the launch.py file in the folder of your server ( ' + ServerName + ')')



			elif ServerBase == '2':
				clear()
				BoucleServer=False
				versionwant1=Ch_Vanilla()
				clear()
				print('We are downloading the server files, Please wait a few seconds .')
				download('http://92.222.88.229/msm/launch.py',pathact+ '/' + 'launch.py' )
				download(versionwant1[0] , pathact + ServerName+'.jar')
				print('pathact')
				fichier = open(pathact + '/' + 'name.info', 'w')
				fichier.write(ServerName +'\n'+ ServerBase +'\n'+ versionwant1[1])
				fichier.close()
				print('To start the server the server, launch the zero.py file in the folder ' + ServerName)
			else:
				BoucleServer = True
				clear()
				print('Please enter a correct value !!')
			

			wait(2)
			clear()
			print('Now the program go start the server, press Ctrl + c for interupt the program !!')
			wait(2)
			clear()
			exit(0)



	while  contpathserv:
		if pathserver == 'y' or pathserver == 'Y':
			contpathserv = True
			pathtrue = True
			if not os.path.exists(ServerName):
				os.mkdir(ServerName)

			pathcourrant()

		elif pathserver == 'N' or pathserver == 'n':
			clear()
			pathact = input("Please enter the path of your server \n  Example of path: \n    For Linux: /home/yourself/Documents \n    For Windows: C:/Users/yourself/Documents \n \n but please do not enter the name of your server,\n he go be create by this program \n Your Path:   ")
			while pathtrue:
				print("see")
				if os.path.exists(pathact)==False:
					clear()
					pathact = input("Sorry but you enter a false path \n Please try agaon  \n Your Path:   ")
				elif os.path.exists(pathact)==True:
					print("Your Server gona be create in : " + pathact + "/" + ServerName)
					contpathserv = False
					pathtrue = False

					if not os.path.exists(pathact + "/" + ServerName):
						os.mkdir(pathact + "/" + ServerName)
						BoucleServer=True
					pathact = pathact + '/' + ServerName  + '/'
					pathchoose()




if __name__ == '__main__':
	main()









############################
