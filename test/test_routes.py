import unittest
from app import app

class TestFlaskRoutes(unittest.TestCase):

    def setUp(self):
        """Set up the test client"""
        app.config['TESTING'] = True
        app.config['SESSION_TYPE'] = 'filesystem'
        self.client = app.test_client()

    def test_home_page(self):
        """Test if the homepage loads correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_current_account_page(self):
        """Test if the current account creation page loads"""
        response = self.client.get('/current_account')
        self.assertEqual(response.status_code, 200)

    def test_savings_account_page(self):
        """Test if the savings account creation page loads"""
        response = self.client.get('/savings_account')
        self.assertEqual(response.status_code, 200)

    def test_exit_app(self):
        """Test if the exit page loads"""
        response = self.client.post('/exit')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
