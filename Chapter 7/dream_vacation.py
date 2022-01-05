active=True
poll={}

while active:
	name=input("Name: ")
	vacation=input("Place to visit: ")
	poll[name]=vacation
	more=input("Anyone else? ")
	if more.lower() == 'no':
		active=False

print("\n-----Poll results-----")
for name, place in poll.items():
	print(f"{name.title()} wants to visit {place.title()}.")