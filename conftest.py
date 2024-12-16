import pytest

from api_client.weather_api_client import ApiClient
from utils.data_handler import DataHandler

data_handler = DataHandler()

@pytest.fixture(scope='session', params=data_handler.load_requests('current'))
def current_request_data(request):
    yield request.param

@pytest.fixture(scope='session', params=data_handler.load_requests('current'))
def forecast_request_data(request):
    yield request.param

@pytest.fixture(scope='session')
def api_client():
    return ApiClient(data_handler.uri)