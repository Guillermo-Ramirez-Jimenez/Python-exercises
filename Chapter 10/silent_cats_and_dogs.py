print("Some famous cats:")
try:
	with open("text_files/cats.txt") as f:
		print(f.read())
except FileNotFoundError:
	pass

print("\nSome famous dogs:")
try:
	with open("text_files/dogs.txt") as f:
		print(f.read())
except FileNotFoundError:
	pass