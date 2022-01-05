dog={
	'kind':'dog',
	'owner':'bart',
	}

cat={
	'kind':'cat',
	'owner':'lisa',
	}

iguana={
	'kind':'iguana',
	'owner':'shelma',
	}

pets=[dog, cat, iguana]

for pet in pets:
	print()
	for key, value in pet.items():
		print(f"{key.title()}: {value.title()}")