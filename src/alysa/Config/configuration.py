#/usr/bin/python3
import sys
sys.path.append("src/")
from .commandlist import *
import json

class Setup:
	def __init__(self):
		pass
	
	#setup command
	def command(self):
		path_list = []
		json_list = [] # element of json_list: {"saySomething" : {"OS" : ["Windows"], "languages" : ["en"], "prefix" : ["say"]}}
		
		#convert json data to our data format
		data = {} # data format: {"say" : {"OS" : ["Windows"], "function" : saySomething, "languages" : ["en"]. "play" : ....}
		# this format allows us to find command with O(1)
	
		# list_command = [(path_json, function, function_name)]
		for x in list_command:
			path = x[0]
			function_name = x[2]
			try:
				index = path_list.index(path)
			except:
				a = open(path, "r")
				path_list.append(path)
	
				my_json = json.load(a)
				json_list.append(my_json)
	
				index = path_list.index(path)
	
			# now transform the data
			f = json_list[index][function_name] # f = {"OS" : ["Windows"], "languages" : ["en"], "prefix" : ["say"]}
			my_prefix = f["prefix"] # my_prefix = ["say", ...]
			f.pop("prefix") # remove field prefix from f
			for p in my_prefix:
				f["function"] = x[1] # the function pointer, f = {"OS" : ["Windows"], "languages" : ["en"], "function" : Command.defaultcommand.saySomething]}
				data[p] = f # add f to the field p in data
			
		return data
	
	#setup useless words of a languages
	def uselessWords(self, langs = "en"):
		"""langs = name of the language: 'fr' 'en' 'es'
		return a list of useless words"""

		data_file = open("res/Langs/uselesswords.json", "r")
		data = json.load(data_file) # data = {"en" : {"preposition" : ["at"], "verb" : []}, "fr": ...}
		languages = data[langs] # choose the list of useless words in the languages chosen to reduce space
		useless_list = []
		for word in languages:
			useless_list.extend(languages[word]) # extend useless_list with another list
		return useless_list
