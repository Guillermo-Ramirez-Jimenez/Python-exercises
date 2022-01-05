def make_sandwich(*args):
	print("The sandwich will include:")
	for item in args:
		print(f"-{item.title()}")

make_sandwich("cheese", "tuna", "bacon")