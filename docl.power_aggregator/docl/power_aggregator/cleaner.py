def clean_raw_productions(raw_productions: dict) -> list:
    """
    Fill missing data in productions time series
    """
    return [
        {
            'name': raw_production['name'],
            'production': clean_raw_production(raw_production['production']),
            'dt': raw_production['dt']
        } for raw_production in raw_productions
        ]

def clean_raw_production(raw_production: list) -> list:
    """
    Fill missing data in production time series
    """
    production = [raw_production[0]]
    for first, second in zip(raw_production, raw_production[1:]):
        if first['end'] != second['start']:
            production.append({
                'start': first['end'],
                'end': second['start'],
                'power': (first['power'] + second['power'])/2
            })
        production.append(second)
    
    return production