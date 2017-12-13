__author__ = 'ar.chusovitin'
import unittest
from datetime import datetime
import api.converter_json as cj


class TestConverter(unittest.TestCase):

    def test_datatime(self):
        time = datetime(2017, 1, 2)
        json = {"Date": time}

        new_json = cj.converter(json)

        self.assertEqual(new_json, '{"Date": "02.01.2017"}')
