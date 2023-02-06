# -*- coding: utf-8 -*-

from datetime import datetime

from docl.power_aggregator.exporter import VALID_FORMATS

def check_params(args: dict):                                                               
    """                                                                            
    Check parameters                                                   
    """                                                                            
    check_date(args['from'])
    check_date(args['to'])
    check_format(args['format'])

def check_date(date_as_string: str):
    """
    Check that date_as_string matches DD-MM-YYYY format
    """
    datetime.strptime(date_as_string, '%d-%m-%Y').date()

def check_format(format: str):
    """
    Check that format is supported
    """
    if (format not in VALID_FORMATS):
        raise ValueError(f"Wrong format, should be one of {VALID_FORMATS}")

def check_config(config: dict):
    """
    Check that config is valid
    """
    check_config_key(config, 'url')
    check_config_key(config, 'power_plants')

def check_config_key(config, key):
    """
    Check that config key is valid
    """
    if not config[key]:
        raise ValueError(f"Configuration must contain attribute '{key}'")
