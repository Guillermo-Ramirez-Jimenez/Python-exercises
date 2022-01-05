import json

filename="text_files/favorite_number.json"

try:
	with open(filename) as f:
		number=json.load(f)
except FileNotFoundError:
	print("File not found.")
else:
	print(f"I know your favorite number! It's {number}!")