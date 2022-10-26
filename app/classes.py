import datetime
import json
import requests
import urllib.request
from http import HTTPStatus


class FileMixin:
    def __init__(self):
        self.file_name = "weather_forecast"

    def write_json(self, data: object) -> None:
        """Write data to json."""

        with open(f"files/{self.file_name}.json", "a") as f:
            json.dump(data, f, indent=6)

    def read_json(self) -> None:
        """Read data from json file."""

        try:
            with open(f"files/{self.file_name}.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise e
        else:
            return data


class ConnectionMixin:
    def __init__(self, localization) -> None:
        self.localization = localization
        self.url = f'http://api.weatherapi.com/v1/current.json?'
        self.api_key = 'key=542f7d3a3b87476f8a7160752222110'

    def build_url(self) -> str:
        localization_format = self.localization.replace(" ", "_")
        request_url = f'{self.url}{self.api_key}{localization_format}'
        return request_url

    def connect_to_api(self) -> bool:
        url: str = self.build_url()
        response = requests.get(url)
        # TODO CHECK COMPARE STATUS CODES INSTEAD OF STRINGS
        if response.status_code == HTTPStatus.OK:
            return True
        return False

    def get_data_to_dict(self) -> dict:
        url = self.build_url()
        get_data = urllib.request.urlopen(url)
        return get_data


class WeatherForecast:
    def __init__(self):
        self.forecast = {}
        self.data = datetime.datetime.now()
