class User:
	"""Describes a user."""

	def __init__(self, first_name, last_name, **kwargs):
		self.first_name=first_name
		self.last_name=last_name
		self.data=kwargs
		self.login_attempts=0

	def describe_user(self):
		print(f"\nName: {self.first_name.title()} {self.last_name.title()}")
		for key, value in self.data.items():
			print(f"\t{key.title()}: {value}")

	def greet_user(self):
		print(f"\nHi {self.first_name.title()} {self.last_name.title()}.")

	def increment_login_attempts(self):
		self.login_attempts+=1

	def reset_login_attempts(self):
		self.login_attempts=0

	def get_login_attempts(self):
		return self.login_attempts


homer=User("homer", "simpson", age=39, hair="bald", workplace="nuclear plant")
homer.increment_login_attempts()
homer.increment_login_attempts()
print(homer.get_login_attempts())
homer.reset_login_attempts()
print(homer.get_login_attempts())