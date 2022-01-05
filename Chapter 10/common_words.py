filename="text_files/dracula.txt"
word=' the '

try:
	with open(filename, encoding="utf-8") as f:
		text=f.read()
		words=text.split()
		print(f"The word '{word.strip()}' shows up {text.count(word)} times.")
		print(
			f"The word '{word.strip()}' or '{word.strip().title()}' "
			"shows up {text.lower().count(word)} times."
			)

except FileNotFoundError:
	print(f"'{filename}' not found.")