import csv
import json

import functools


CSV = 'csv'
JSON = 'json'

VALID_FORMATS = [CSV, JSON]

def export(aggregated_production: list, output_format: str):
    """
    Export aggregated production to the wanted format
    """
    if output_format == CSV:
        export_csv(aggregated_production)
    elif output_format == JSON:
        export_json(aggregated_production)

def write_csv_line(e):
    """
    Write a production csv line
    """
    return str(e['start']) + ';' + str(e['end']) + ';' + str(e['power']) + '\n'

def export_csv(aggregated_powers: list):
    """
    Export aggregated production to csv
    """
    print("start;end;power\n" + functools.reduce(lambda a, b: a+b, [write_csv_line(e) for e in aggregated_powers]))

def export_json(aggregated_powers: list):
    """
    Export aggregated production to json
    """
    print(json.dumps(aggregated_powers, indent=2))