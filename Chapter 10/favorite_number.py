import json

filename="text_files/favorite_number.json"

try:
	number=int(input("Write your favorite number: "))
except:
	print("That's not a number!")	
else:
	with open(filename, 'w') as f:
		json.dump(number, f)