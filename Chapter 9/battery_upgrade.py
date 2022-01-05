class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size=battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def upgrade_battery(self):
		"""Replace the current battery with a 100 one."""
		self.battery_size=100


class Car:
	"""Stripped down Car class."""

	def __init__(self, make, model, year):
		"""Initialize car."""
		self.make=make
		self.model=model
		self.year=year


class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery=Battery()

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery.battery_size==75:
			bat_range=260
		elif self.battery.battery_size==100:
			bat_range=315
		print(f"This car can go about {bat_range} miles on a full charge.")


new_car=ElectricCar("Tesla", "Model S", 2021)

new_car.battery.describe_battery()
new_car.get_range()

new_car.battery.upgrade_battery()

new_car.battery.describe_battery()
new_car.get_range()