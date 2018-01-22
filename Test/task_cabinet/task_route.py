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


class TestRegistration(unittest.TestCase):

    def test_get(self):
        data = json.loads(rq.get('{url}/cabinet'.format(url=URL)).text)
        self.assertEqual(data[names.ANSWER], names.SUCCESS)

    def test_event_get_page_error(self):
        data = json.loads(rq.get('{url}/cabinet?id=text'.format(url=URL)).text)
        self.assertEqual(data[names.ANSWER], names.ERROR)