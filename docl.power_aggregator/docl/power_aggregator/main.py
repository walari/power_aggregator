# -*- coding: utf-8 -*-

import logging
from argparse import ArgumentParser
from yaml import safe_load

from docl.power_aggregator.retriever import get_productions

from docl.power_aggregator.cleaner import clean_raw_productions

from docl.power_aggregator.exporter import export

from docl.power_aggregator.aggregator import synchronize_productions, check_synchronized_productions, aggregate_productions

from docl.power_aggregator.utils.check import check_params, check_config

CONFIG_PATH = "config.yml"

def main():

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger("docl.power_aggregator")

    logger.info("Start")

    parser = ArgumentParser(description="Process end to end test on DWIB")
    parser.add_argument('--from', required=True, help='beggining of period DD-MM-YYYY')
    parser.add_argument('--to', required=True, help='end of period DD-MM-YYYY')
    parser.add_argument('--format', required=True, help='output format, json or csv')

    args = vars(parser.parse_args())
    
    config = None
    with open(CONFIG_PATH, "r") as f:
        config = safe_load(f)
    
    check_params(args)
    check_config(config)

    start_date = args['from']
    end_date = args['to']
    output_format = args['format']

    # Retrieve productions from API
    raw_productions = get_productions(config['url'], config['power_plants'], start_date, end_date)
    
    # Fill missing data in productions
    productions = clean_raw_productions(raw_productions)
    
    # Synchronize production to 900s dt
    synchronized_productions = synchronize_productions(productions)

    # Check that synchronized productions can be aggregated (start timestamps must match)
    check_synchronized_productions(synchronized_productions)

    # Check that synchronized productions can be aggregated (start timestamps must match)
    aggregated_productions = aggregate_productions(synchronized_productions)

    export(aggregated_productions, output_format)


if __name__ == "__main__":
    main()
