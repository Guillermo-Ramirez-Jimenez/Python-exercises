numbers=[]

for x in range(1_000_000):
	numbers.append(x+1)

print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")