def stage_of_life(age):
	if(age<2):
		print("Baby")
	elif(age<4):
		print("Toddler")
	elif(age<13):
		print("Kid")
	elif(age<20):
		print("Teenager")
	elif(age<65):
		print("Adult")
	elif(age>=65):
		print("Elder")

stage_of_life(1)
stage_of_life(3)
stage_of_life(10)
stage_of_life(15)
stage_of_life(25)
stage_of_life(70)