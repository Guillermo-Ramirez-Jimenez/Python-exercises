class User:
	"""Describes a user."""

	def __init__(self, first_name, last_name, **kwargs):
		self.first_name=first_name
		self.last_name=last_name
		self.data=kwargs

	def describe_user(self):
		print(f"\nName: {self.first_name.title()} {self.last_name.title()}")
		for key, value in self.data.items():
			print(f"\t{key.title()}: {value}")

	def greet_user(self):
		print(f"\nHi {self.first_name.title()} {self.last_name.title()}.")


homer=User("homer", "simpson", age=39, hair="bald", workplace="nuclear plant")
homer.describe_user()
homer.greet_user()

bart=User("bart", "simpson", age=10, hair="blonde", job="student")
bart.describe_user()
bart.greet_user()