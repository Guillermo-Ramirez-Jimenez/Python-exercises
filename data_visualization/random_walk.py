from random import choice
import math

class RandomWalk:
	"""A class to generate random walks."""

	def __init__(self, num_points=5000):
		"""Initialize attributes of a walk."""
		self.num_points = num_points

		# All walks start at (0, 0).
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Calculate all the points in the walk."""

		# Keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:

			x_step = self.get_step()
			y_step = self.get_step()

			# Reject moves that go nowhere.
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the new position.
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)

	def get_step(self):
		"""Calculate the step in one direction."""
		# Decide which direction to go and how far to go in that direction.
		length = [x for x in range(5)]

		direction = choice([1, -1])
		distance = choice(length)
		step = direction * distance

		return(step)

	def fill_walk_polar(self):
		"""Calculate all the points in the walk in polar coords."""

		# Keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:

			x_step, y_step = self.get_step_polar()

			# Calculate the new position.
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)

	def get_step_polar(self):
		"""Calculate the steps in each direction in polar coords."""
		# Decide which angle to rotate and how far to go in that direction.
		angle = choice([x for x in range(0, 360, 30)])
		radius = choice([1, 2, 3, 4])
		
		x_step = radius * math.cos(math.radians(angle))
		y_step = radius * math.sin(math.radians(angle))

		return(x_step, y_step)