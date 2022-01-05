filename="text_files/guest_book.txt"

with open(filename, "w") as file:
	while True:
		name=input("\nEnter 'q' to quit\nEnter a guest name: ")
		if name=='q':
			break
		print(f"Welcome {name}.")
		file.write(name+"\n")