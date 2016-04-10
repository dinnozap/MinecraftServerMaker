import subprocess, os, zipfile, requests

## Function Download
def download(url, fichier):
 pass
 fileName = fichier
 req = requests.get(url)
 file = open(fileName, 'wb')
 for chunk in req.iter_content(100000):
     file.write(chunk)
 file.close()
 print("The download is finish !")
## Function Unzip
def unzip(source , destination):
 with zipfile.ZipFile(source) as zf:
  zf.extractall(destination)

nameinfo = open("name.info", "r")

ServerName = nameinfo.readline().rstrip()
Version = nameinfo.readline().rstrip()
VersionServer = nameinfo.readline().rstrip()

nameinfo.close()

subprocess.call(['java', '-jar', ServerName +'.jar'])


fichier = open("eula.txt", "w")
fichier.write("eula = true")
fichier.close()
if not os.path.exists("world"):
	print("Whitch type of Minecraft server you want to create ?")
	a=input("[1] Pre-Build (Map and Plugin) Spigot Server [2]  Blanc Spigot Server [3] Sem-Build (Plugin prebuild) : ")
	if a == '1':
	 print(VersionServer)
	 if VersionServer == '1.9' or VersionServer == '1.8' or VersionServer == '1.7.10':
	  download('http://puu.sh/ocXv2/ef4b3abc59.zip', 'world.zip')
	  unzip('world.zip', '')
	  if not os.path.exists("plugins"):
	          os.mkdir("plugins")
	  download('https://hub.spigotmc.org/jenkins/job/Spigot-Essentials/lastSuccessfulBuild/artifact/Essentials/target/Essentials-2.x-SNAPSHOT.jar', 'plugins/essentials.jar')
	  download('https://www.spigotmc.org/resources/sexymotd.2474/download?version=73466', 'plugins/motd.jar')
	  subprocess.call(['java', '-jar', ServerName +'.jar'])
	elif a=='2':
	 subprocess.call(['java', '-jar', ServerName +'.jar'])
	elif a=='3':
		download('https://hub.spigotmc.org/jenkins/job/Spigot-Essentials/lastSuccessfulBuild/artifact/Essentials/target/Essentials-2.x-SNAPSHOT.jar', 'plugins/essentials.jar')
		download('https://www.spigotmc.org/resources/sexymotd.2474/download?version=73466', 'plugins/motd.jar') 
		subprocess.call(['java', '-jar', ServerName +'.jar'])
