import json
from difflib import get_close_matches

data = json.load(open("data.json"))

try:
	def translate(word):
		word = word.lower()
		if word in data:
			return data[word]
		elif word.title() in data:
			return data[word.title()]
		elif word.upper() in data:
			return data[word.upper()]
		elif len(get_close_matches(word , data.keys())) > 0 :
			print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
			decide = input("press yes or no: ")
			if decide == "yes":
				return data[get_close_matches(word , data.keys())[0]]
			elif decide == "no":
				return("please double check spelling...")
			else:
				return("You have entered wrong input please enter just yes or no")
		else:
			print("sorry - word not in dictionary")



	word = input("Enter the word you want to search: ")
	result = translate(word)
	if type(result) == list:
		for word in result:
			print(word)
	else:
		print(result)
except KeyboardInterrupt:
	print("Good Bye...")
	exit()