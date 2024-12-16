"""Setup testing data"""
import json
from dataclasses import dataclass

from api_client.weather_api_request import WeatherAPIRequest

@dataclass
class TestData:
    """Data object for testing"""
    request: WeatherAPIRequest
    expected: dict

class DataHandler:
    """Read testing data and prepare requests for tests"""
    _DATA_PATH = 'data/weatherAPI_test_data.json'
    _URI_PATH = 'data/weather_API_endpoint.json'

    def load_requests_json(self):
        """load requests structure"""
        with open( self._DATA_PATH) as data:
            return json.load(data)

    def load_requests(self, uri_filter=''):
        """Create filtered requests list"""
        requests = self.load_requests_json()
        return [WeatherAPIRequest(**req) for req in requests if uri_filter in req.get('uri')]

    @property
    def uri(self):
        """load uri value"""
        with open( self._URI_PATH) as data:
            uri_data = json.load(data)
            return uri_data.get('uri')
