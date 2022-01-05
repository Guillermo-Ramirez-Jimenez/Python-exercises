pizzas=["bacon","tuna", "bbq"]
friend_pizzas=pizzas[:]

pizzas.append("veggie")
friend_pizzas.append("4 cheeses")

print("My favourite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)