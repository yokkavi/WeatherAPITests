import json
from symtable import Class

from api_client.weather_API_request import WeatherAPIRequest


class DataHandler:
    _DATA_PATH = 'data/weatherAPI_test_data.json'
    _URI_PATH = 'data/weather_API_endpoint.json'

    def load_requests_json(self, uri_filter=''):
        with open( self._DATA_PATH) as data:
            return json.load(data)

    def load_requests(self, uri_filter=''):
        requests = self.load_requests_json(uri_filter)
        return [WeatherAPIRequest(**req) for req in requests if uri_filter in req.get('uri')]

    @property
    def uri(self):
        with open( self._URI_PATH) as data:
            uri_data = json.load(data)
            return uri_data.get('uri')

    def setup_data(self, uri_filter, test_data):
        requests_jsons = self.load_requests_json(uri_filter)
        data_tuples = []
        for req in requests_jsons:
            if uri_filter in req.get('uri'):
                for data_set in test_data:
                    req_pars = WeatherAPIRequest(**req)
                    req_pars.update_params(**data_set[0])
                    data_tuples.append((req_pars, data_set[1]))
        return data_tuples


class TestData:
    request: WeatherAPIRequest
    expected: dict