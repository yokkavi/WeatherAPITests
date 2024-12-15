from datetime import datetime, timedelta

import pytest
from api_client.weather_API_client import ApiClient

from utils.data_handler import DataHandler as DataHandler

# TODO create requests enum based on requirements ('forecast', 'future' etc) and
#  use it in data_handler.get_requests('current') as filter
data_handler = DataHandler()

test_data = [
    ({'q': 'Paris', 'lang': 'en'}, {'name': 'Paris'}),
    ({'q': 'London', 'lang': 'fr'}, {'name': 'London'}),
    ({'q': 'Moscow', 'lang': 'ru'}, {'name': 'London'}),
    ({'q': 'Incorrect', 'lang': 'ru'}, {'name': ''}),
]


@pytest.fixture(scope='session')
def api_client():
    return ApiClient(data_handler.uri)


@pytest.fixture(scope='session', params=data_handler.setup_data('forecast', test_data))
def forecast_request(request):
    yield request.param


def test_current_weather_API(forecast_request, api_client):
    res = api_client.send_request(forecast_request)
    assert res.status_code == 200

# @pytest.mark.parametrize("param,expected", setup_testing_data('forecast'))
# def test_forecast_weather_API(param, expected, api_client):
#     res = api_client.send_request(param)
#     assert res.status_code == 200