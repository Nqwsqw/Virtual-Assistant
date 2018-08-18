import sys
sys.path.append("src/")
from alysa.Command import defaultcommand

list_command = [
	("src/alysa/Command/tags.json", defaultcommand.printHello, "printHello"),
	("src/alysa/Command/tags.json", defaultcommand.saySomething, "saySomething"),
	("src/alysa/Command/tags.json",
defaultcommand.playMusic, "playMusic"),
]