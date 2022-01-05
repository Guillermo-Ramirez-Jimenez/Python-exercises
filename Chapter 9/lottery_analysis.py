from random import randint, choice
from string import ascii_letters

numbers=10
letters=5
selected=4

items=[]
for x in range(numbers):
	items.append(randint(0, 9))
for x in range(letters):
	items.append(choice(ascii_letters))

my_ticket=[]
for x in range(selected):
	my_ticket.append(choice(items))

tries=0
won=False
while won==False:
	selection=[]
	for x in range(selected):
		selection.append(choice(items))
	if selection==my_ticket:
		won=True
	tries+=1

print(f"It took {tries} tries until you won with ticket:\n\t{my_ticket}")