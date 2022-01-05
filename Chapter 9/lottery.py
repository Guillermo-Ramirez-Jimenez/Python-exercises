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

selection=[]
for x in range(selected):
	selection.append(choice(items))

print(f"The ticket: {selection} won the price!")