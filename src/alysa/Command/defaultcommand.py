def printHello(request):
	print("Hello World")

def saySomething(request):
	string = request["raw"]
	string = request.split("say ")
	string = string[1]
	print(string)
