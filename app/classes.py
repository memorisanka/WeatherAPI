import urllib.request
import requests


class FileMixin:
    pass


class ConnectionMixin:
    def __init__(self, localization):
        self.localization = localization
        self.url = f'http://api.weatherapi.com/v1/current.json?'
        self.api_key = 'key=542f7d3a3b87476f8a7160752222110'

    def build_url(self):
        localization_format = self.localization.replace(" ", "_")
        request_url = f'{self.url}{self.api_key}{localization_format}'
        return request_url

    def connect_to_api(self):
        url = ConnectionMixin.build_url(self)
        response = requests.get(url)
        if response == 'Response<200>':
            return response

    def get_data_to_dict(self):
        url = ConnectionMixin.build_url(self)
        get_data = urllib.request.urlopen(url)
        # data = json.loads(self.response.read())
        return get_data


class WeatherForecast:
    pass
