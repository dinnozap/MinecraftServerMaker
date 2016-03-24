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
