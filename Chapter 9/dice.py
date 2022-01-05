from random import randint

class Die:
	"""Simulates a die."""

	def __init__(self, sides=6):
		self.sides=sides

	def roll_die(self):
		print(randint(1, self.sides))


print("\n6 sides die:")
die6=Die()
for x in range(10):
	die6.roll_die()

print("\n10 sides die:")
die10=Die(10)
for x in range(10):
	die10.roll_die()

print("\n20 sides die:")
die20=Die(20)
for x in range(10):
	die20.roll_die()