import unittest
from app import create_app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_ping_endpoint(self):
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'pong')

    def test_fizzbuzz_endpoint(self):
        response = self.client.get('/fizzbuzz')
        self.assertEqual(response.status_code, 200)
        fizzbuzz_results = response.json['results']
        expected_results = []
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                expected_results.append('FizzBuzz')
            elif i % 3 == 0:
                expected_results.append('Fizz')
            elif i % 5 == 0:
                expected_results.append('Buzz')
            else:
                expected_results.append(str(i))
        self.assertEqual(fizzbuzz_results, expected_results)

if __name__ == '__main__':
    unittest.main()
