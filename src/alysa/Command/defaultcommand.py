import os
import platform
from playsound import playsound
from subprocess import call

def printHello(request):
	print("Hello World")

def saySomething(request):
	string = request["raw"]
	string = request.split("say ")
	string = string[1]
	print(string)

def playMusic(request):
	string = request["auto"]
	string = string.replace("play ", "")
	extension = "mp3"
	path = "res/Musics/" + string + "." + extension
	music = open(path, "r")
	if(os.path.isfile(path) == True):
		playsound(path)
	else:
		print("No Such Music")

def openApp(request):
	string = request["auto"]
	string = string.replace("open ", "")
	extension = ["app", "exe"]
	if(platform.system == "Windows"):
		call([string + extension[1]])
	if(platform.system == "Darwin"):
		call([string +extension[0]])
	if(platform.system == "Linux"):
		os.system(string)
	else:
		print("Unknow operating system")
		
		
		