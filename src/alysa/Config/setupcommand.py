import sys
sys.path.append("src/")
from .commandlist import *
import json

def setup():
	path_list = []
	json_list = []
	data = {} # data sample: {"say" : {"OS" : ["Windows"], "function" : saySomething, "languages" : ["en"]}
	for x in list_command:
		path = x[0]
		try:
			index = path_list.index(path)
			function_name = x[2]
			f = json_list[index][function_name]
			my_dict = f
			my_dict.pop(my_dict["prefix"])
			my_dict["function"] = x[1]
			for y in f["prefix"]:
				data[y] = my_dict
		except:
			file = open(path, "r")
			data = json.load(file)
			path_list.append(path)
			json_list.append(data)
	return data