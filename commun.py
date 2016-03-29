import time
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
	b = a[0] + "." + a[2]
	print(a)
	a = str(b) + ''
	version1 = "https://s3.amazonaws.com/Minecraft.Download/versions/"+a+"/minecraft_server."+a+".jar"
	print(version1)
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