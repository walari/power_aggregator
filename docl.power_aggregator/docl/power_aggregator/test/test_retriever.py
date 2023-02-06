import unittest

from docl.power_aggregator.retriever import format_csv_production, format_json_production


class RetrieverTest(unittest.TestCase):

    def test_format_csv_production(self):
        response_text = """debut,fin,valeur
        1578006000,1578009600,568
        1578009600,1578013200,770
        1578013200,1578016800,754"""

        power_plant_config = {
            'start_field': 'debut',
            'end_field': 'fin',
            'power_field': 'valeur',
            'format': 'csv',
            'sep': ','
        }

        expected_production = [
            {
                'start': 1578006000,
                'end': 1578009600,
                'power': 568
            },
            {
                'start': 1578009600,
                'end': 1578013200,
                'power': 770
            },
            {
                'start': 1578013200,
                'end': 1578016800,
                'power': 754
            }
        ]

        production = format_csv_production(response_text, power_plant_config)

        self.assertTrue(expected_production == production)


    def test_format_json_production(self):
        response_text = """[
            {
                "start_time":1578006000,
                "end_time":1578007800,
                "value":774
                },
            {
                "start_time":1578007800,
                "end_time":1578009600,
                "value":682
            },
            {
                "start_time":1578009600,
                "end_time":1578011400,
                "value":622
            }]"""

        power_plant_config = {
            'start_field': 'start_time',
            'end_field': 'end_time',
            'power_field': 'value',
            'format': 'json'
        }

        expected_production = [
            {
                'start': 1578006000,
                'end': 1578007800,
                'power': 774
            },
            {
                'start': 1578007800,
                'end': 1578009600,
                'power': 682
            },
            {
                'start': 1578009600,
                'end': 1578011400,
                'power': 622
            }
        ]

        production = format_json_production(response_text, power_plant_config)

        self.assertTrue(expected_production == production)
