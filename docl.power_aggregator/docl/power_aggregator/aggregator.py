import functools

REFERENCE_DT = 900

def synchronize_productions(productions: list) -> list:
    """
    Synchronized productions using same reference dt
    """
    return [
        {
            'name': production['name'],
            'production': adapt_production_dt(production['production'], production['dt']),
        } for production in productions
    ]

def adapt_production_dt(production: list, original_dt: int) -> list:
    """
    interpolate production time series so dt matched reference dt.
    """
    return [
        item 
        for production_point in production
        for item in adapt_production_point_dt(production_point, original_dt//REFERENCE_DT)
    ]

def adapt_production_point_dt(production_point: dict, factor: int) -> list:
    """
    interpolate a single production time series point.
    """
    return [
        (production_point['start'] + i*REFERENCE_DT,production_point['power']) for i in range(factor) 
    ]

def check_synchronized_productions(synchronized_productions: list):
    """
    Check that all production time series have the expected structure, they must start at the same time and have the same length.
    Given that missing data has already been filled at this stage, it ensures that aggregation can be done.
    """
    min_start_dates = [synchronized_production['production'][0][0] for synchronized_production in synchronized_productions]
    production_lengths = [len(synchronized_production['production']) for synchronized_production in synchronized_productions]
    if not all_equals(min_start_dates):
        raise ValueError("Can't aggregate productions, start dates don't match")
    if not all_equals(production_lengths):
        raise ValueError("Can't aggregate productions, lengths differ")

def all_equals(l: list) ->  bool:
    """
    Return true if all elements in list are equal.
    """
    return all([e == l[0] for e in l])

def aggregate_productions(synchronized_productions: list) -> list:
    """
    Aggregate all synchronized productions
    """
    timestamps = [production_point[0] for production_point in synchronized_productions[0]['production']]
    aggregated_production = functools.reduce(
        add_synchronized_productions,
        [[production_point[1] for production_point in synchronized_production['production']] for synchronized_production in synchronized_productions ])
    return [{
        "start": timestamp,
        "end": timestamp + REFERENCE_DT,
        "power": power
        } for timestamp, power in zip(timestamps, aggregated_production)]

def add_synchronized_productions(production_a: list, production_b: list) -> list:
    return [value_a+value_b for value_a, value_b in zip(production_a, production_b)]
