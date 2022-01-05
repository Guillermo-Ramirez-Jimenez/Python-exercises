favourite_fruits=["melon", "banana", "orange"]

def check_favourite_fruit(fruit):
	if(fruit.lower() in favourite_fruits):
		print(f"You like {fruit.lower()}!")
	else:
		print(f"You don't like {fruit.lower()}!")

check_favourite_fruit("Melon")
check_favourite_fruit("Apple")