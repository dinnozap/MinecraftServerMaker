# -*- coding: utf-8 -*-
########################################
### Minecraft Server Maker #############
### Create Your Own Minecraft Server ###
########################################

from commun import *
import os

os.remove("install.py")
bcl = 1
nbnotfound = 1
clear()
while bcl:

	print("###############################\n### Minecraft Server Maker ###\n##############################")
	a=input("[1] Create Server [2] Quit : ")




	if a == "1":
		clear()
		print("Starting creation of the server")
		load(4)
		import base
		bcl = 0




	elif a == "2":
		print("Good Bye ;)")
		wait(1)
		clear()
		exit(0)



	else:
		clear()
		print("Command not found\n:(")
		print("Error #", nbnotfound)
		nbnotfound += 1

	if nbnotfound > 20:
		print("Sorry but the program gona shutdown beceause you enter 20 false result !!!!! :/")
		wait(2)
		clear()
		print("Good Bye")
		exit(0)