favourite_places={
	'Homer':['Jamaica'],
	'Marge':['France', 'Italy', 'Greece'],
	'Bart':['Romania', 'Mexico'],
	}

for person, places in favourite_places.items():
	print(f"\n{person} likes:")
	for place in places:
		print(f"\t{place}")