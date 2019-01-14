"""
This project creates a simple command-line searchable dictionary that returns word definitions 
using data from a JSON file
"""

import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDefinition():
	userInput = input("Please type a word/phrase to search or \q to quit: ")
	if(userInput != "\q"):
		userInput = userInput.lower()
		tempMatch = get_close_matches(userInput,data.keys())
		if(userInput in data):
			print("\nDefinition: %s\n" % data[userInput][0])
			getDefinition()
		elif(len(tempMatch) > 0):
			word = tempMatch[0]
			followup = input("Did you mean : " + word + " ? Y - to get definition, any other character to continue: ")
			if(followup.lower() == "y"):
				print("\nDefinition: %s\n" % data[word][0])
				getDefinition()
			else:	
				getDefinition()
		else:
			print("\nNo results found! Check spelling and try again.\n")
			getDefinition()
	else:
		print("\nSimple Dictionary will now terminate. Thanks")
		return

getDefinition()