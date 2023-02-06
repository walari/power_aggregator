import unittest

from docl.power_aggregator.aggregator import adapt_production_point_dt


class AggregatorTest(unittest.TestCase):

    def test_adapt_production_point_dt(self):
        production_point = {
                "start": 1578006000,
                "end": 1578006000+3600,
                "power": 710
            }
        factor = 4
        expected_production = [
            (1578006000, 710),
            (1578006000+900, 710),
            (1578006000+1800, 710),
            (1578006000+2700, 710)
        ]

        production = adapt_production_point_dt(production_point, factor)

        self.assertTrue(expected_production == production)
