import os
import glob
import platform
import webbrowser
from playsound import playsound
from subprocess import call
from bs4 import BeautifulSoup
from os.path import join
from googlesearch import search

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
	extension = "exe"
	if(platform.system() == "Windows"):
		app = string + "." + extension
		for root, dirs, files in os.walk("C:\\"):
			if app in files:
				path = os.path.join(root, app)
			os.startfile(path)
	elif platform.system() == "Darwin":
		os.system("open -a" + string)
	elif platform.system() == "Linux":
		os.system(string)
	else:
		print("Unknow operating system")
		
def searchOnWeb(request):
	string = request["auto"]
	string = string.replace("search on web ", "")
	for url in search(string, tld='com', lang='fr', num=5, start=0, stop=5, pause=0):
		print(url)
	
		
		
		
