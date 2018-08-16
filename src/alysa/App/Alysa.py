import sys
sys.path.append("src/")
from alysa.Config import setupcommand

class Alysa:
	def __init__(self, data = setupcommand.setup(), useless_list = ["ok"]):
		self.data = data
		self.useless_list = useless_list

	def runCommand(self, string):
		new_string = self.keepUsefulWords(self.useless_list, string)

		# select command
		tag = self.selectCommand(new_string)
		my_dict = self.data[tag] # dict that contain command info

		request = {"auto" : new_string, "raw" : string}
		try:
			my_dict["function"](request) # run command
		except Exception as e:
			print(e)

	def selectCommand(self, string):
		""" Select the right command
		beta phase"""
		string = string.split(" ")
		tag = string[0]
		return tag

	def keepUsefulWords(self, useless_list, string):
		pass

	def reply(self):
		pass

def main():
	alysa = Alysa()

if __name__ == '__main__':
	main()