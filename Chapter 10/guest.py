name=input("Write your name: ")

with open("text_files/guest.txt", "w") as file:
	file.write(name+"\n")
