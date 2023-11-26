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

if __name__ == '__main__':
    unittest.main()
