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


class Admin(User):
	"""Manages the admin user."""

	def __init__(self, first_name, last_name, **kwargs):
		super().__init__(first_name, last_name, **kwargs)
		self.privileges=Privileges()
		self.privileges.add_privilege("can add post")
		self.privileges.add_privilege("can delete post")
		self.privileges.add_privilege("can ban user")
		

class Privileges:
	"""Manages the privileges."""

	def __init__(self):
		self.privileges=[]

	def show_privileges(self):
		return(self.privileges)

	def add_privilege(self, privilege):
		self.privileges.append(privilege)