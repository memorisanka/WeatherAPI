from datetime import date
import json
import requests
import os
import urllib.request
from http import HTTPStatus


class FileMixin:
    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def check_directory() -> None:
        """Check if directory exists."""

        if not os.path.isdir(os.getcwd() + "/files"):
            os.mkdir(os.getcwd() + "/files")

    def check_file(self) -> bool:
        """Check if file exists."""

        return os.path.exists(os.getcwd() + f"/files/{self.file_name}.json")

    def write_json(self, data: object) -> None:
        """Write data to json."""

        self.check_directory()
        with open(f"files/{self.file_name}.json", "w") as f:
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
        self.url = f"http://api.weatherapi.com/v1/current.json?"
        self.api_key = "key=542f7d3a3b87476f8a7160752222110"

    def build_url(self) -> str:
        """Build url after delete white space between words."""

        localization_format: str = self.localization.replace(" ", "_")
        request_url: str = f"{self.url}{self.api_key}&q={localization_format}"
        return request_url

    def connect_to_api(self) -> bool:
        """Build url and connect to API"""

        url: str = self.build_url()
        response = requests.get(url)
        if response.status_code == HTTPStatus.OK:
            return True
        return False

    @staticmethod
    def set_data() -> str:
        """Set today's date."""

        today: date = date.today()
        time_stamp: str = today.strftime("%d/%m/%Y")
        return time_stamp

    def get_data_to_dict(self) -> dict:
        """Build url, add time stamp to data and save to dictionary."""

        url = self.build_url()
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read())
            time_stamp = self.set_data()
            data["time_stamp"] = time_stamp
        return data


class WeatherForecast:
    def __init__(self, file_name) -> None:
        self.forecast = {}
        self.date = date.today()
        self.file_name = file_name

    def check_date(self, forecast) -> bool:
        """Check if today's date is the same as in a saved file."""

        time_stamp: str = self.set_date()
        self.forecast = forecast
        if time_stamp == forecast["time_stamp"]:
            return True
        return False

    def set_date(self) -> str:
        """Return today's date."""

        time_stamp: str = self.date.strftime("%d/%m/%Y")
        return time_stamp

    def show(self):
        """Return a list of forecast positions."""

        forecast: dict = {
            "localization" : self.forecast['location']["name"],
            "country": self.forecast['location']["country"],
            "created_at": self.forecast["time_stamp"],
            "local_time": self.forecast['location']["localtime"],
            "temperature": self.forecast['current']["temp_c"],
            "per_temp": self.forecast['current']["feelslike_c"],
            "wind_speed:": self.forecast['current']["wind_kph"],
            "wind_direction": self.forecast['current']["wind_dir"],
            "pressure:": self.forecast['current']["pressure_mb"],
        }
        return forecast

    def write_forecast(self):
        """Write forecast (dictionary) to JSON file."""

        with open(f"files/{self.file_name}.json", "r") as f:
            self.forecast = json.load(f)
