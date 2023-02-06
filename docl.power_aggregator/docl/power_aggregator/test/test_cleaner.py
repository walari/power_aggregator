import unittest

from docl.power_aggregator.cleaner import clean_raw_production


class CleanerTest(unittest.TestCase):

    def test_clean_raw_production(self):
        raw_production = [
            {
                "start": 1578006000,
                "end": 1578006900,
                "power": 710
            },
            {
                "start": 1578007800,
                "end": 1578008700,
                "power": 518
            },
            {
                "start": 1578008700,
                "end": 1578009600,
                "power": 750
            }
        ]

        expected_production = [
            {
                "start": 1578006000,
                "end": 1578006900,
                "power": 710
            },
            {
                "start": 1578006900,
                "end": 1578007800,
                "power": (710+518)/2
            },
            {
                "start": 1578007800,
                "end": 1578008700,
                "power": 518
            },
            {
                "start": 1578008700,
                "end": 1578009600,
                "power": 750
            }
        ]

        production =  clean_raw_production(raw_production)

        self.assertTrue(expected_production == production)
