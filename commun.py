import time
import requests

def log(logs):
	print("[LOG]:  ", logs)
	logfil = open("log0.log", "a")
	logfil.write("[LOG]:  "+logs+"\n")
	logfil.close()

def clear():
	print("\n" * 100)

def wait(sec):
	time.sleep(sec) 



	
def server(version):
	a = version
	print(a)
	b = a[0] +"." + a[2] 
	if len(a) >  3:
		b = a[0] + "." + a[2] +"."+ a[3]
	a = str(b) + ''
	print(a)	
	version1 = "https://s3.amazonaws.com/Minecraft.Download/versions/"+a+"/minecraft_server."+a+".jar"
	print("\n\nYour Version: " + a)
	print("Link of your version :" + version1 + "\n" *4)

	return version1

def load(sec):
	sec1 = 0
	while sec1 < sec:
		sec1 += 1


		wait(0.125)
		clear()
		print("Loading")
		print("...")
		wait(0.125)
		clear()
		print("Loading")
		print("....")
		wait(0.125)
		clear()
		print("Loading")
		print("....")
		wait(0.125)
		clear()
		print("Loading")
		print(".....")
		wait(0.125)
		clear()
		print("Loading")
		print("......")
		wait(0.125)
		clear()
		print("Loading")
		print("..")
		wait(0.125)
	clear()

def download(url, fichier):
	pass
	fileName = fichier
	req = requests.get(url)
	file = open(fileName, 'wb')
	for chunk in req.iter_content(100000):
	    file.write(chunk)
	file.close()
	print("The download is finish !")

def Ch_Vanilla():
		serv=input("Please enter the version of your futur server (1.x or 1.x.x) :")
		if len(serv) > 3:
			print(serv)
			serv= serv[0] + serv[1] + serv[2] +serv[4]
		else:
			pass
		serv1 = float(serv)
		if serv1 < 1.4:
		        print("Sorry but the versions under 1.4 are not in charge by MCSM")
		        exit(0)

		elif serv1 >= 1.4:
			versionwant=server(serv)
		return versionwant, serv


a1 = "http://getspigot.org/jenkins/job/Spigot/46/artifact/spigot-1.9.jar"
b2= "http://getspigot.org/jenkins/job/Spigot/2/artifact/spigot-1.8.jar"
c3 ="http://getspigot.org/spigot/spigot-1.7.10-R0.1-SNAPSHOTBuild1646.jar"
def Ch_Spigot():
	serv1=input("Please enter the version of your futur server (1.9 or 1.8 or 1.7.10) :")
	if serv1 == "1.9":
		versionwant1 = a1
	elif serv1 == "1.8":
		versionwant1 = b2
	elif serv1 == "1.7.10":
		versionwant1 = c3
	return versionwant1, serv1
