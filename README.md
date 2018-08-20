# Virtual-Assistant

## Prequesties
 - python3
 - playsound python3
 - pyobjc

## Install
```
./install.sh
```

## Add your own command
Go to src/alysa/Command/defaultcommand.py
Add your own function:
 - need a parameter request: `request = {"auto" : new-string, "raw" : old-string}`
 - new-string is the string that we removed all useless words, and old-string is the whole input
 - Then add information of your function in src/alysa/Command/tags.json
 - Then add your function in src/alysa/Config/commandlist.py

Example:
defaultcommand.py:
```python
def saySomething(request):
	string = request["auto"] # take the string that removed all useless words
	print(string) #
```

commandlist.py:
```python
from alysa.Command import defaultcommand
list_command = [
	("src/alysa/Command/tags.json", defaultcommand.saySomething, "saySomething")
]
```

## Run
```
./run.sh
```

or

```
run.bat
```
