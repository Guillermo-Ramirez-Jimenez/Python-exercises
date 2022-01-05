glossary={
	'list':'group of elements, mutable.',
	'tuple':'group of elements, immutable.',
	}

for x in glossary:
	print(f"-{x.title()}:")
	print(f"{glossary.get(x)}\n")