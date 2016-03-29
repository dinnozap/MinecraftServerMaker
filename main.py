# -*- coding: utf-8 -*-
########################################
### Minecraft Server Maker #############
### Create Your Own Minecraft Server ###
########################################

from commun import *

bcl = 1
nbnotfound = 1
while bcl:
	pass
	clear
	print("###############################\n### Minecraft Server Maker ###\n##############################")
	a=input("[1] Create Server [2] Start Server [3] Quit : ")




	if a == "1":
		clear()
		print("Starting creation of the server")
		load(4)
		import base
		bcl = 0



	elif a == "3":
		print("Good Bye ;)")
		exit(0)



	else:
		clear()
		print("Command not found\n:(")
		print("Error #", nbnotfound)
		nbnotfound += 1
