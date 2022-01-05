import json

def greet_user():
	"""Greet the user by name."""
	username=get_stored_username()
	correct=input(f"Is your username {username} (y/n)? ")
	if username and correct.lower()=='y':
		print(f"Welcome back {username}!")
	else:
		username=get_new_username()
		print(f"We'll remember you when you come back, {username}!")
		

def get_stored_username():
	"""Get stored username if available."""
	filename="text_files/username.json"
	try:
		with open(filename) as f:
			username=json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username


def get_new_username():
	"""Prompt for a new username."""
	username=input("What is your name? ")
	filename="text_files/username.json"
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username


greet_user()