import json

filename="text_files/favorite_number.json"

def get_number(filename):
	try:
		with open(filename) as f:
			return(json.load(f))
	except FileNotFoundError:
		return None

def save_number(filename):
	while True:
		try:
			number=int(input("Write your favorite number: "))
		except:
			print("That's not a number!")	
		else:
			with open(filename, 'w') as f:
				json.dump(number, f)
			break

number=get_number(filename)
if number:
	print(f"I know your favorite number! It's {number}!")
else:
	save_number(filename)