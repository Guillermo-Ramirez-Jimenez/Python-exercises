filename="text_files/learning_python.txt"

with open(filename) as file:
	print(file.read())

with open(filename) as file:
	for line in file:
		print(line.strip())

with open(filename) as file:
	lines=file.readlines()
for line in lines:
	print(line.strip())