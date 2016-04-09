##-------- Base Function -------------
def clear():
	print("\n" * 100)
clear()
##----------------- Librairies  
import os, sys, requests, zipfile, shutil
from threading import Thread
##------------------ Interaction -----------

continu = True
iwant = input("The program \'Install.py\' go download all the files, do you want to continue ? Y/N : ")
while continu:
	if iwant == "Y" or iwant == "y":
		continu = False
		clear()
	elif iwant == "N" or iwant == "n":
		continu = False
		clear()
		exit(0)
	else:
		clear()
		iwant = input("Enter a correct value \n The program \'Install.py\' go download all the files, do you want to continue ? Y/N : ")


##-------------Create the tmp folder --------
if not os.path.exists("tmp"):
	os.mkdir("tmp")

##------------- Function ---------

def download(url, fichier):
	print("Start of the download !!")
	fileName = 'tmp/' + fichier
	req = requests.get(url)
	file = open(fileName, 'wb')
	for chunk in req.iter_content(100000):
		file.write(chunk)
	file.close()
	print("The download is finish !")

def unzip(source , destination):
	with zipfile.ZipFile(source) as zf:
		zf.extractall(destination)



##------------ Path Install.py ------

pathname = os.path.dirname(sys.argv[0])        
pathact = os.path.abspath(pathname) + "/"
print( pathact)

##---------------- Download + Unzip + Copy ----------

Thread(download("https://github.com/dinnozap/MinecraftServerMaker/archive/master.zip", "MinecraftServerMaker.zip")).start()
print("Téléchargement du fichier..")
os.mkdir("MSM")
unzip('tmp/MinecraftServerMaker.zip', '/MSM')

src = "MinecraftServerMaker-master/"
for fic in os.listdir(src):
	shutil.copy2(os.path.join(src, fic),pathact)

#------------- Delete TMP, Unzip Archive, Start Main

shutil.rmtree("tmp")
shutil.rmtree("MinecraftServerMaker-master")

print("Now please start main.py in the MSM folder")
exit=("Enter any word or key to exit")
