import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	"""Tests basic functions of the Employee class."""

	def setUp(self):
		"""Initial config."""
		self.employee=Employee("homer", "simpson", 24_000)
		self.amount=1200

	def test_give_default_raise(self):
		"""Tests if the default raise works."""
		self.employee.give_raise()
		self.assertEqual(self.employee.salary, 29_000)

	def test_give_custom_raise(self):
		"""Tests if the custom raise works."""
		self.employee.give_raise(self.amount)
		self.assertEqual(self.employee.salary, 25_200)


if __name__=='__main__':
	unittest.main()