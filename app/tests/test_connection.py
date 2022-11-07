from app.classes import ConnectionMixin
import requests
import unittest
from app.properties import API_KEY


class TestAPI(unittest.TestCase):
    URL = f"http://api.weatherapi.com/v1/current.json?"
    api_key = API_KEY

    def test_should_return_401(self):
        """Test should return 401, because of no authorization (no api_key)"""

        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 401)

    def test_should_return_200(self):
        """If url is valid, test should return 200"""

        localization = 'Berlin'
        url = f"{self.URL}{self.api_key}&q={localization}"
        resp = requests.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_should_return_true(self):
        """Test should return True, because there is such city as Berlin."""

        conn = ConnectionMixin('Berlin')
        self.assertTrue(conn.connect_to_api())

    def test_should_return_false(self):
        """Test should return False, because there is no such city as ababcd."""

        conn = ConnectionMixin('ababcd')
        self.assertFalse(conn.connect_to_api())


if __name__ == '__main__':
    test = TestAPI()
