topping=""
active=True
while active:
	topping=input("Enter next topping: ")
	if topping.lower() != 'quit':
		print(f"Added {topping.lower()}.")
	else:
		active=False