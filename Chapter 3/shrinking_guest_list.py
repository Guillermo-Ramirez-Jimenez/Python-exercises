import math

names=["homer", "marge", "bart", "lisa", "maggie"]

for x in names:
	print(f"Hi {x.title()}, you have been invited to my party.")

modified=2
print(f"Unfortunately, {names.pop(modified).title()} cannot assist.")
new_guest="abe"
print(f"Fortunately, {new_guest.title()} will come.")
names.insert(modified, new_guest)

for x in names:
	print(f"Hi {x.title()}, you have been invited to my party.")

print("We have more guests!")
more_guests=["otto", "flanders", "dr. nick"]
names.insert(0, more_guests[0])
names.insert(math.ceil(len(names)), more_guests[1])
names.append(more_guests[2])

for x in names:
	print(f"Hi {x.title()}, you have been invited to my party.")

limit=2
print(f"Sorry, but only {limit} guests are allowed.")
for x in range(len(names)-limit):
	print(f"Hi {names.pop().title()}, you are not invited.")
for x in names:
	print(f"Hi {x.title()}, you are still invited to my party.")
for x in range(len(names)):
	del names[x-1]
print(names)