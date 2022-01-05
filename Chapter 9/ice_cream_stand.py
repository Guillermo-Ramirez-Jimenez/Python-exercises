from restaurant import Restaurant

class IceCreamStand(Restaurant):
	"""Models an ice cream stand, which is also a restaurant."""

	def __init__(self, name):
		super().__init__(name, "ice creams")
		self.flavors=[]

	def add_flavor(self, new_flavor):
		self.flavors.append(new_flavor)

	def get_flavors(self):
		return self.flavors


ice_cream_store=IceCreamStand("ice cream store")
ice_cream_store.add_flavor("chocolate")
ice_cream_store.add_flavor("vanilla")
print(ice_cream_store.get_flavors())
ice_cream_store.describe_restaurant()