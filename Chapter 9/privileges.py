from users import User
from privileges_module import Privileges

class Admin(User):
	"""Manages the admin user."""

	def __init__(self, first_name, last_name, **kwargs):
		super().__init__(first_name, last_name, **kwargs)
		self.privileges=Privileges()
		self.privileges.add_privilege("can add post")
		self.privileges.add_privilege("can delete post")
		self.privileges.add_privilege("can ban user")


admin=Admin("over", "lord", power="over 9000")
admin.describe_user()
print(admin.privileges.show_privileges())