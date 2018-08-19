import sys
sys.path.append("src/")
from .commandlist import *
import json

def setup():
	path_list = []
	json_list = [] # element of json_list: {"saySomething" : {"OS" : ["Windows"], "languages" : ["en"], "prefix" : ["say"]}}
	data = {} # data sample: {"say" : {"OS" : ["Windows"], "function" : saySomething, "languages" : ["en"]}

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
		my_prefix = f["prefix"]
		f.pop("prefix")
		for p in my_prefix:
			f["function"] = x[1] # the function not the name of function
			data[p] = f
		
	return data
