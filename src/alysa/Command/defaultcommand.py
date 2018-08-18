import os
from playsound import playsound

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
	path = "Virutal-Assistant/res/Musics/" + string + "." + extension
	music = open(path, "r")
	if(os.path.isfile(path) == True):
		playsound(path)
	else:
		print("No Such Music")