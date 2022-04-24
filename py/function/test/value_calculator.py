import unittest
from datetime import datetime

from py.function.values_calc import ValueCalculator


class ValueCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.vc = ValueCalculator()

    def test_correct_response(self):
        response = self.vc.calculate_vals('67352', '2010')

        self.assertIn('MarketValue', response)
        self.assertIn('AuctionValue', response)

        self.assertIsInstance(response['MarketValue'], float)
        self.assertIsInstance(response['AuctionValue'], float)

    def test_future_year(self):
        future_year = datetime.now().year + 1
        response = self.vc.calculate_vals('67352', str(future_year))

        self.assertIn('error', response)
        self.assertEqual(response['error'], "No data for future years")

    def test_ne_model(self):
        response = self.vc.calculate_vals('67358', '2010')

        self.assertIn('error', response)
        self.assertEqual(response['error'], "No such ID in data")

    def test_ne_year(self):
        response = self.vc.calculate_vals('67352', '2022')

        self.assertIn('error', response)
        self.assertEqual(response['error'], "No data for given year")
