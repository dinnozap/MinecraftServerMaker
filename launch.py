import subprocess
from name import *
subprocess.call(['java', '-jar', ServerName +'.jar'])

fichier = open("eula.txt", "w")
fichier.write("eula = true")
fichier.close()

subprocess.call(['java', '-jar', ServerName +'.jar'])
