cities={
	'madrid':{
			'country':'spain',
			'beach':'no',
		},
	'new york':{
			'country':'usa',
			'beach':'yes',
		},
	'moscow':{
			'country':'russia',
			'beach':'no',
		},
	}

for city, data in cities.items():
	print(f"\n{city.title()}:")
	for key, value in data.items():
		print(f"\t{key.title()}: {value.title()}")