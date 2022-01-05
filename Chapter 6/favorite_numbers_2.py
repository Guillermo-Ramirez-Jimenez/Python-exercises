favourite_numbers={
	'homer':[1],
	'marge':[2, 3],
	'bart':[4, 5, 6],
	'lisa':[7, 8, 9],
	'maggie':[0],
	}

for person, numbers in favourite_numbers.items():
	print(f"\n{person.title()} likes:")
	for number in numbers:
		print(f"\t{number}")