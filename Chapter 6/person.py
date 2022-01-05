homer={
	'first_name':'Homer',
	'last_name':'Simpson',
	'age':39,
	'city':'Springfield',
	}

for x in homer:
	print(f"{x}: {homer.get(x)}")