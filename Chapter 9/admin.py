from users import User

class Admin(User):
	"""Manages the admin user."""

	def __init__(self, first_name, last_name, **kwargs):
		super().__init__(first_name, last_name, **kwargs)
		self.privileges=["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		return(self.privileges)


admin=Admin("over", "lord", power="over 9000")
admin.describe_user()
print(admin.show_privileges())