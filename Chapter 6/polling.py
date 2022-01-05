favourite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

polling=['jen','sarah','pepe','paco']

for name in polling:
	if(name in favourite_languages.keys()):
		print(f"Thank you for taking the poll, {name.title()}")
	else:
		print(f"Please, complete the poll {name.title()}")