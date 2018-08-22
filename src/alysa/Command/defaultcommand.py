import os
import glob
import platform
import webbrowser
import wikipedia
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
	extension = [".ink", ".exe"]
	if(platform.system() == "Windows"):
		exeFile = string + extension[1]
		inkFile = string + extension[0]
		for x in ("C:\ProgramData\Microsoft\Windows\Start Menu\Programs", "C:\Program Files (x86)", "C:\Program Files", os.getenv('LOCALAPPDATA'), os.getenv('APPDATA')):
			for root, dirs, files in os.walk(x):
				if inkFile in files:
					path = os.path.join(root, inkFile)
					os.startfile(path)
					return
				if exeFile in files:
					path = os.path.join(root, exeFile)
					os.startfile(path)
					return							
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
		
def searchOnWiki(request):
        string = request["raw"]
        string = string.replace("search on wiki ", "")
        print(wikipedia.summary(string, sentences=5))
	
		
		
		
