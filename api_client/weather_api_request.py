"""https://app.swaggerhub.com/apis-docs/WeatherAPI.com/WeatherAPI/1.0.2#/APIs/forecast-weather"""

from api_client.weather_api_params import RequestParametersBase, RequestParametersForecast

# TODO create requests enum based on requirements ('forecast', 'future' etc)
# TODO use enum instead if, add exception for empty params

class WeatherAPIRequest:
    """Full request object with attributes"""
    uri: str
    method: str
    headers: str
    uri: str
    params: RequestParametersBase

    def __init__(self, **kwargs):
        self.method = kwargs.get('method')
        self.headers = kwargs.get('headers')
        self.uri = kwargs.get('uri')
        self.params = self.build_request_params(kwargs.get('params'))

    def update_params(self, **kwargs):
        """update params: RequestParametersBase field with kwargs data set"""
        for arg, val in kwargs.items():
            setattr(self.params, arg, val)

    def build_request_params(self, params) -> RequestParametersBase:
        """setup params field depends on uri"""
        if 'forecast' in self.uri and params:
            return RequestParametersForecast(**params)
        return RequestParametersBase(**params)

    def __repr__(self) -> str:
        return (f'WeatherAPIRequest\n'
                f'method: {self.method}\n'
                f'headers: {self.headers}\n'
                f'uri: {self.uri}\n'
                f'params: {self.params}')
