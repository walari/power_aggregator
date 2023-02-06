# power_aggregator
Aggregates power plants production

### Install
Install the power_aggregator application: `pip install -e .\docl.power_aggregator`

### Configure
The configuration is made with the `./conf.yml` file.

### Run

Run example: `python -m docl.power_aggregator.main --from 01-01-2023 --to 02-01-2023 --format json`

Tests example: `python -m unittest discover .\docl.power_aggregator\docl\power_aggregator\test\`