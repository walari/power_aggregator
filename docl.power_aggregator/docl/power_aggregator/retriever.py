import requests
import json
import csv

def get_productions(url: str, power_plants_config: dict, start_date: str, end_date: str) -> list:
    """
    Retrieve productions from solar power plants API
    """
    return [
        {
            'name': power_plant_config['name'],
            'production': get_production(url, power_plant_config, start_date, end_date),
            'dt': power_plant_config['dt']
        } for power_plant_config in power_plants_config
    ]

def get_production(url: str, power_plant_config: dict, start_date: str, end_date: str) -> list:
    """
    Retrieve production from solar power plants API
    """
    production = []
    power_plant_name = power_plant_config['name']
    power_plant_url = f"{url}{power_plant_name}"
    try:
        response = requests.get(
            url = power_plant_url,
            params = {'from': {start_date}, 'to': {end_date}})
        if response.status_code == 200:
            production = format_production(response.text, power_plant_config)
        else:
            print(f"Failed to retrieve data from power plant {power_plant_name}")
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to establish connection with power plant api ({power_plant_url})")
        raise
    except requests.exceptions.HTTPError as e:
        print(f"Didn't receive status 200, we cannot perform aggregation since data will be missing")
        raise                 

    return production

def format_production(response_text: str, power_plant_config: dict) -> list:
    """
    Format retrieved production in a standard list
    """
    production = []
    if power_plant_config['format'] == 'csv':
        production = format_csv_production(response_text, power_plant_config)
    elif power_plant_config['format'] == 'json':
        production = format_json_production(response_text, power_plant_config)
    else:
        print(f"Unknown format : {power_plant_config['format']}")
    return production

def format_csv_production(response_text: str, power_plant_config: dict) -> list:
    """
    Format retrieved production as csv in a standard list
    """
    response_lines = response_text.splitlines()[1:]
    rows = csv.reader(response_lines, delimiter=power_plant_config['sep'])
    production = [{'start': int(row[0]),'end': int(row[1]),'power': int(row[2])} for row in rows]

    return production

def format_json_production(response_text: str, power_plant_config: dict) -> list:
    """
    Format retrieved production as json in a standard list
    """
    return json.loads(response_text, object_hook=lambda item: format_json_item_production(item, power_plant_config))

def format_json_item_production(item: dict, power_plant_config) -> dict:
    return {
        'start': item[power_plant_config['start_field']],
        'end': item[power_plant_config['end_field']],
        'power': item[power_plant_config['power_field']]}