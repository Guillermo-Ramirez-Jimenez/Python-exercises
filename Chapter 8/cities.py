def describe_city(city, country="Spain"):
	"""Describes the specified city in the specified country."""
	print(f"{city.title()} is in {country.title()}.")

describe_city("tokyo", "japan")
describe_city("rome", "italy")
describe_city("madrid")