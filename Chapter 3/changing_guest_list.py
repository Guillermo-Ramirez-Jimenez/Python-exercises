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