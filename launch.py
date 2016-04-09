import subprocess

nameinfo = open("name.info", "r")

ServerName = nameinfo.readline().rstrip()
Version = nameinfo.readline().rstrip()
VersionServer = nameinfo.readline().rstrip()
nameinfo.close()

subprocess.call(['java', '-jar', ServerName +'.jar'])


fichier = open("eula.txt", "w")
fichier.write("eula = true")
fichier.close()

subprocess.call(['java', '-jar', ServerName +'.jar'])
