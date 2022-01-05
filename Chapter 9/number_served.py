class Restaurant:
	"""Defines and operates a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print(f"Name: {self.restaurant_name.title()}")
		print(f"Cuisine type: {self.cuisine_type}")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name.title()} is now open!")

	def set_number_served(self, number_served):
		self.number_served=number_served

	def increment_number_served(self, inc=1):
		self.number_served+=inc

	def get_number_served(self):
		return f"{self.restaurant_name.title()} has served {self.number_served} customers."


restaurant=Restaurant("rest", "generic")

restaurant.number_served=5
print(restaurant.get_number_served())
restaurant.number_served=8
print(restaurant.get_number_served())

restaurant.set_number_served(10)
print(restaurant.get_number_served())

restaurant.increment_number_served(4)
print(restaurant.get_number_served())