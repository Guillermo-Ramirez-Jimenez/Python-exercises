homer={
	'first_name':'Homer',
	'last_name':'Simpson',
	'age':39,
	'city':'Springfield',
	}

lisa={
	'first_name':'Lisa',
	'last_name':'Simpson',
	'age':8,
	'city':'Springfield',
	}

bart={
	'first_name':'Bart',
	'last_name':'Simpson',
	'age':10,
	'city':'Springfield',
	}


people=[homer, lisa, bart]

for person in people:
	print()
	for key, value in person.items():
		print(f"{key.title()}: {value}")