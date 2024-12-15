from httpx import Client
from utils.logger_utils import logger
from dataclasses import asdict


class ApiClient(Client):

    url = ''
    def __init__(self, uri):
        self.url = uri
        super().__init__(base_url=uri)

    def send_request(self, request):
        method = request.method or 'GET'
        full_url = self.url + request.uri
        logger.info(f'{method} {full_url}\n REQUEST:\n{request.params}\n')
        response = super().request(method=method, url=full_url, params=asdict(request.params))
        logger.info(f'{method} {full_url}\n RESPONSE:\n{response}\n')
        return response