sandwich_orders=["pastrami", "bacon", "pastrami", "tuna", "cheese", "pastrami"]
print(sandwich_orders)

print("No pastrami left.")

while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")

print(sandwich_orders)