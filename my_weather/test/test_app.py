#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/28 2:44
File: test_app.py
Software: PyCharm
"""
import json
import unittest
from weather import app
class FlaskTesting(unittest.TestCase):
    def create_app(self):
        app.config.update(TESTING=True)
        return app

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/adminapi/get_weather_information?adCode=440306')
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()