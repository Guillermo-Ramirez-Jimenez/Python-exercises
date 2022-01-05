class Restaurant:
	"""Defines and describes a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(f"Name: {self.restaurant_name.title()}")
		print(f"Cuisine type: {self.cuisine_type}")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name.title()} is now open!")


bohio=Restaurant("bohio", "traditional")
bohio.describe_restaurant()
bohio.open_restaurant()