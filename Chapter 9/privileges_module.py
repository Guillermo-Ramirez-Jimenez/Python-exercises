class Privileges:
	"""Manages the privileges."""

	def __init__(self):
		self.privileges=[]

	def show_privileges(self):
		return(self.privileges)

	def add_privilege(self, privilege):
		self.privileges.append(privilege)