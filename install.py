import os, sys, requests, zipfile, shutil


if not os.path.exists("preserver"):
	os.mkdir("preserver")

def download(url, fichier):
	print("Start of the download !!")
	fileName = 'preserver/' + fichier
	req = requests.get(url)
	file = open(fileName, 'wb')
	for chunk in req.iter_content(100000):
		file.write(chunk)
	file.close()
	print("The download is finish !")

def unzip(source , destination):
	with zipfile.ZipFile(source) as zf:
		zf.extractall(destination)

pathname = os.path.dirname(sys.argv[0])        
pathact = os.path.abspath(pathname) + "\\"
print( pathact)


download("https://github.com/dinnozap/MinecraftServerMaker/archive/master.zip", "MinecraftServerMaker.zip")
unzip('preserver/MinecraftServerMaker.zip', '')

src = "MinecraftServerMaker-master/"
for fic in os.listdir(src):
	shutil.copy2(os.path.join(src, fic),pathact)
shutil.rmtree("preserver")
shutil.rmtree("MinecraftServerMaker-master")
import main.py