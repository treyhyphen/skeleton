"""Run a unit test.

Credit to https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
"""
import os
import unittest
import json

from application import app


class BasicTests(unittest.TestCase):
    """setup and teardown."""

    def setUp(self):
        """Execute prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
        # self.assertEqual(app.config[''])

    def tearDown(self):
        """Execute after each test."""
        pass

    def run_tests(self):
        """Run tests."""
        unittest.main(verbosity=2)

    def test_main_page(self):
        """Test main page."""
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Test</title>', response.data, msg='Make sure global variables got loaded from env')

    def test_api_sup_world(self):
        """Test sup_world method."""
        response = self.app.get('/api/sup_world', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Sup, World?', json.loads(response.data)['msg'], msg='Make sure sup_world API responds with appropriate strings')
