print("Let's add two numbers.")
try:
	number1=int(input("Enter first number: "))
	number2=int(input("Enter second number: "))
except ValueError:
	print("That's not a number!")
else:
	print(f"Result: {number1+number2}")