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
        min_val = 1
        max_val = 15
        response = self.client.get(f'/fizzbuzz/{min_val}/{max_val}')
        self.assertEqual(response.status_code, 200)
        fizzbuzz_results = response.json['results']
        expected_results = []
        for i in range(min_val, max_val + 1):
            if i % 3 == 0 and i % 5 == 0:
                expected_results.append('FizzBuzz')
            elif i % 3 == 0:
                expected_results.append('Fizz')
            elif i % 5 == 0:
                expected_results.append('Buzz')
            else:
                expected_results.append(str(i))
        self.assertEqual(fizzbuzz_results, expected_results)

    def test_fizzbuzz_endpoint_error(self):
        min_val = 15
        max_val = 10
        response = self.client.get(f'/fizzbuzz/{min_val}/{max_val}')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid range: min must be less than or equal to max')

    def test_fibonacci_endpoint(self):
        max_val = 10
        response = self.client.get(f'/fibonacci/{max_val}')
        self.assertEqual(response.status_code, 200)
        expected_sequence = [0, 1, 1, 2, 3, 5, 8]
        self.assertEqual(response.json['sequence'], expected_sequence)

    def test_large_fibonacci_endpoint(self):
        max_val = 100000000000000000000000
        response = self.client.get(f'/fibonacci/{max_val}')
        self.assertEqual(response.status_code, 200)
        sequence = response.json['sequence']
        # We check if the last two numbers are below the max_val and their sum is above max_val
        self.assertTrue(sequence[-1] <= max_val)
        self.assertTrue(sequence[-2] <= max_val)
        self.assertTrue(sequence[-1] + sequence[-2] > max_val)

    def test_factorial_endpoint(self):
        n = 5
        response = self.client.get(f'/factorial/{n}')
        self.assertEqual(response.status_code, 200)
        expected_result = 1
        for i in range(2, n + 1):
            expected_result *= i
        self.assertEqual(response.json['result'], expected_result)

    def test_factorial_endpoint_error(self):
        n = -5
        response = self.client.get(f'/factorial/{n}')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid input: n must be non-negative')

if __name__ == '__main__':
    unittest.main()
