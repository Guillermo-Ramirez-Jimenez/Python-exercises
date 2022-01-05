import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
	"""Tests the city, country function."""

	def test_city_country(self):
		"""Tests the simple case: Santiago, Chile"""
		test=city_country("santiago", "chile")
		self.assertEqual(test, "Santiago, Chile")

	def test_city_country_population(self):
		"""Tests the simple case: Santiago, Chile - population 5000000"""
		test=city_country("santiago", "chile", population=5_000_000)
		self.assertEqual(test, "Santiago, Chile - population 5000000")


if __name__=='__main__':
	unittest.main()