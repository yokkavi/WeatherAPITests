from dataclasses import dataclass
#TODO add more requests

@dataclass
class RequestParametersBase:
    """Based on https://www.weatherapi.com/docs/
    request parameters"""
    key: str
    q: str
    lang: str = 'ru'


@dataclass
class RequestParametersForecast(RequestParametersBase):
    """ Based on
    https://app.swaggerhub.com/apis-docs/WeatherAPI.com/WeatherAPI/1.0.2#/APIs/forecast-weather
    request parameters"""
    dt: str = ''
    unixdt: str = '' #pass 'dt' or 'unixdt'
    hour: str = ''
    alerts: str = 'no'    #alerts=yes or alerts=no
    aqi: str = 'no'       #aqi=yes or aqi=no
    tp: str = '15'

    def __setattr__(self, prop, val):
        if prop == "unixdt" and val and self.dt:
            raise ValueError("Please either pass 'dt' or 'unixdt' "
                             "and not both in same request")

        super().__setattr__(prop, val)
