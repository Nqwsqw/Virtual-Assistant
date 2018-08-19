#Virtual-Assistant

##Prequesties
 - python3
 - playsound python3
 - pyojbc

##Add your own command
Go to src/alysa/Command/defaultcommand.py
Add your own function:
 - need a parameter request: request = {"auto" : new-string, "raw" : old-string}
 - new-string is the string that we removed all useless words, and old-string is the whole input

Example:
```python
def saySomething(request):
	string = request["auto"] # take the string that removed all useless words
	print(string) #
```

## Run
```
./run.sh
```
