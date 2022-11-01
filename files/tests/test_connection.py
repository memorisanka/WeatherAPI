from app.classes import ConnectionMixin
import requests
import unittest


class TestAPI(unittest.TestCase):
    url = f"http://api.weatherapi.com/v1/current.json?"
    api_key = "key=542f7d3a3b87476f8a7160752222110"

    def test_should_return_401(self):
        """Test should return 401, because of no authorization (no api_key)"""

        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 401)
        print('Test 1 completed')

    def test_should_return_200(self):
        """Test should return 200, because url is valid"""

        localization = 'Berlin'
        url = f"{self.url}{self.api_key}&q={localization}"
        resp = requests.get(url)
        self.assertEqual(resp.status_code, 200)
        print('Test 2 completed')

    def test_should_return_true(self):
        """Test should return True, because there is such city as Berlin."""

        conn = ConnectionMixin('Berlin')
        self.assertTrue(conn.connect_to_api())
        print('Test 3 completed')

    def test_should_return_false(self):
        """Test should return False, because there is no such city as ababcd."""

        conn = ConnectionMixin('ababcd')
        self.assertFalse(conn.connect_to_api())
        print('Test 4 completed')


if __name__ == '__main__':
    test = TestAPI()

    test.test_should_return_401()
    test.test_should_return_200()
    test.test_should_return_true()
    test.test_should_return_false()
