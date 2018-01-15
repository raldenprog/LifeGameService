__author__ = 'ar.chusovitin'
import json
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../app/api')
sys.path.append(os.getcwd()+'/../app/route')
import unittest
import requests as rq
from app.api.service import GameService as gs

URL = 'http://127.0.0.1:13451'
#URL = 'http://87.103.243.110:13451'


class TestEventRoute(unittest.TestCase):

    def test_event_get(self):
        data = json.loads(rq.get('{url}/event'.format(url=URL)).text)
        print(data)
        self.assertEqual(data[names.ANSWER], 'Success')

    def test_event_get_page(self):
        data = json.loads(rq.get('{url}/event?page=1'.format(url=URL)).text)
        self.assertEqual(data[names.ANSWER], 'Success')
        test_dict_answer = {'name': 'Test_event', 'description': 'test', 'status': '1', 'date_start': '04.12.2017', 'date_end': '04.12.2017'}
        self.assertEqual(data['Data'][0], test_dict_answer)

    def test_event_get_page_error(self):
        data = json.loads(rq.get('{url}/event?page=text'.format(url=URL)).text)
        self.assertEqual(data[names.ANSWER], names.ERROR)

    def test_event_get_all(self):
        data = json.loads(rq.get('{url}/event'.format(url=URL)).text)
        self.assertEqual(data[names.ANSWER], 'Success')
        #self.assertEqual(data['Data'], dict())

    def test_event_find_event(self):
        data = json.loads(rq.get('{url}/event?q=text'.format(url=URL)).text)
        self.assertEqual(data[names.ANSWER], 'Success')
        # self.assertEqual(data['Data'], dict())

    def test_event_current_event(self):
        data = json.loads(rq.get('{url}/event?page=1&current=1'.format(url=URL)).text)
        self.assertEqual(data[names.ANSWER], 'Success')
        # self.assertEqual(data['Data'], dict())