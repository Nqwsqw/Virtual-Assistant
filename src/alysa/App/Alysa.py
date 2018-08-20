import sys
sys.path.append("src/")
from alysa.Config.configuration import Setup

class Alysa:
	def __init__(self, data = Setup().command(), useless_list = Setup().uselessWords()):
		self.data = data # data = {"say" : {"OS" : ["Windows", "Mac OS"], "languages" : ["en"], "function" : saySomething()}}
		self.useless_list = useless_list # useless_list = ["to", "at", "in", "please"] useless words

	def runCommand(self, string):
		new_string = self.keepUsefulWords(self.useless_list, string)

		# select command
		tag = self.selectCommand(new_string)
		
		try:
			#my_dict = {"OS" : ["Windows", "Mac OS"], "languages" : ["en"], "function" : saySomething()}
			my_dict = self.data[tag]
			request = {"auto" : new_string, "raw" : string} # because maybe the dev want to use the string with useless words
			my_dict["function"](request) # run command
		except Exception as e:
			print(e)
			
	def selectCommand(self, string):
		""" Select the right command
		beta phase"""
		string = string.split(" ")
		tag = string[0]
		return tag

	# We need to remove useless words in order to select the right command
	def keepUsefulWords(self, useless_list, string):
		""""return the new string without useless words"""
		for words in useless_list:
			if words in string and words in useless_list:
				string = string.replace(words, "")
				string = string.strip()
		return string
	
	def reply(self):
		pass

