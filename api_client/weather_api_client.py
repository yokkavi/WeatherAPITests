"""Client module"""
from dataclasses import asdict
from httpx import Client, Response

from api_client.weather_api_request import WeatherAPIRequest
from utils.logger_utils import logger


class ApiClient(Client):
    """ApiClient class with logging"""
    url = ''
    def __init__(self, uri):
        self.url = uri
        super().__init__(base_url=uri)

    def send_request(self, request: WeatherAPIRequest) -> Response:
        """send request and write a log"""
        method = request.method or 'GET'
        full_url = self.url + request.uri
        logger.info('%s %s\n REQUEST:\n%s\n', method, full_url, request.params)
        response = super().request(method=method, url=full_url, params=asdict(request.params))
        logger.info('RESPONSE: %s\n %s\n', response.status_code, response.text)
        return response

    def send_request_with_params(self, request: WeatherAPIRequest, param: dict) -> Response:
        request.update_params(**param)
        return self.send_request(request)
