vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

car=input("Which car would you like to rent? ")
car=car.lower()

if car[0] in vowels:
	print(f"Let me see if I can find you an {car.title()}.")
else:
	print(f"Let me see if I can find you a {car.title()}.")