age=-1
active=True

while active:
	age=int(input("\nEnter your age:\nYou may quit entering 0\n"))
	if age == 0:
		break
	if age < 3:
		print("You enter free!")
	elif age < 12:
		print("Your price is $10.")
	else:
		print("Your price is $15.")