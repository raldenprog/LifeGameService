__author__ = 'ar.chusovitin'
import json
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../app/api')
sys.path.append(os.getcwd()+'/../app/route')
import unittest
import requests as rq
from app.api.sql import SqlQuery

URL = 'http://127.0.0.1:13451'
#URL = 'http://87.103.243.110:13451'


class TestRegistration(unittest.TestCase):

    def test_event_get(self):
        data = json.loads(json.loads(rq.get('{url}/event'.format(url=URL)).text))
        self.assertEqual(data['Answer'], 'Success')

    def test_event_get_page(self):
        data = json.loads(json.loads(rq.get('{url}/event?page=1'.format(url=URL)).text))
        self.assertEqual(data['Answer'], 'Success')
        test_dict_answer = {'name': 'Test_event', 'description': 'test', 'status': '1', 'date_start': '04.12.2017', 'date_end': '04.12.2017'}
        self.assertEqual(data['Data'][0], test_dict_answer)

    def test_event_get_page_error(self):
        data = json.loads(json.loads(rq.get('{url}/event?page=text'.format(url=URL)).text))
        self.assertEqual(data['Answer'], 'Error')