#!/usr/bin/python
"""
This script retrieves and prints the temperature history data for
a sensor.

To use it, run:
./examples/sensors_history --access_token <SAMSARA_API_TOKEN> --group_id <GROUP_ID> --sensor_id <SENSOR_ID>,

passing in your Samsara API access token, the group ID and sensor ID.

"""
from datetime import datetime
import calendar

import click

import samsara
from samsara.apis import SamsaraClient


@click.command()
@click.option('--access_token', type=str, required=True)
@click.option('--group_id', type=int, required=True)
@click.option('--sensor_id', type=int, required=True)
def get_sensors_history(access_token, group_id, sensor_id):
    # Create an instance of the SamsaraClient.
    client = SamsaraClient()
    # Get a sensor's temperature history at hour-intervals for the past two hours.
    now = datetime.utcnow()
    end_ms = calendar.timegm(now.utctimetuple()) * 1000
    step_ms = 3600000
    start_ms = end_ms - (step_ms * 2)
    series = [{"widgetId": sensor_id, "field": "ambientTemperature"}]
    fill_missing = "withNull"
    params = samsara.HistoryParam(group_id, start_ms, end_ms, step_ms, series, fill_missing)

    history = client.get_sensors_history(access_token, params)
    for result in history.results:
        print '\ntimestamp: {}, series: {}'.format(result.time_ms, result.series)


if __name__ == "__main__":
    get_sensors_history()
