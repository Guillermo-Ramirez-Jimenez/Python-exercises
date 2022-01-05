favourite_numbers={
	'homer':1,
	'marge':2,
	'bart':3,
	'lisa':4,
	'maggie':5,
	}

for x in favourite_numbers:
	print(f"{x.title()}: {favourite_numbers.get(x)}")