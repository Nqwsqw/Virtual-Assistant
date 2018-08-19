#/usr/bin/python3
import json

def setup(langs = "en"):
	"""langs = name of the language: 'fr' 'en' 'es'"""
	data_file = open("res/Langs/uselesswords.json", "r")
	data = json.load(data_file) # data = {"en" : {"preposition" : ["at"], "verb" : []}, "fr": ...}
	languages = data[langs]
	useless_list = []
	for word in languages:
		useless_list.extend(languages[word]) # extend useless_list with another list
	return useless_list
