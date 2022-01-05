filename="text_files/learning_python.txt"

with open(filename) as file:
	for line in file:
		print(line.replace("Python", "C").strip())