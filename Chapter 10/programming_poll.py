filename="text_files/programming_poll.txt"

with open(filename, "w") as file:
	while True:
		reason=input(
			"\nEnter 'q' to quit"
			"\nEnter a reason why you like programming: "
			)
		if reason=="q":
			break
		file.write(reason+"\n")
