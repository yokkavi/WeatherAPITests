"""Test response locations correctness for Weather API service"""
import json
import pytest

# TODO create requests enum based on requirements ('forecast', 'future' etc) and
#  use it in data_handler.get_requests('current') as filter


locations = [
    ({'q': 'Paris', 'lang': 'en'}, {('location', 'name'): 'Paris', ('location', 'country'): 'France'}),
    ({'q': 'London', 'lang': 'fr'}, {('location', 'name'): 'London'}),
    ({'q': 'Moscow', 'lang': 'ru'}, {('location', 'name'): 'Moscow'}),
]

failed_location = [({'q': 'Incorrect', 'lang': 'ru'}, {('location', 'name'): ''})]


@pytest.mark.parametrize("param, expected", locations)
def test_current_weather_API(current_request_data, param, expected, api_client):
    res = api_client.send_request_with_params(current_request_data, param)
    value = json.loads(res.text)
    assert res.status_code == 200
    assert [value[k[0]][k[1]] for k,v in expected.items()] == [i for i in expected.values()]

@pytest.mark.parametrize("param, expected", locations)
def test_forecast_weather_API(forecast_request_data, param, expected, api_client):
    res = api_client.send_request_with_params(forecast_request_data, param)
    value = json.loads(res.text)
    assert res.status_code == 200
    assert [value[k[0]][k[1]] for k,v in expected.items()] == [i for i in expected.values()]

@pytest.mark.xfail
@pytest.mark.parametrize("param, expected", failed_location)
def test_forecast_weather_API(forecast_request_data, param, expected, api_client):
    res = api_client.send_request_with_params(forecast_request_data, param)
    value = json.loads(res.text)
    assert res.status_code == 200
    assert [value[k[0]][k[1]] for k,v in expected.items()] == [i for i in expected.values()]