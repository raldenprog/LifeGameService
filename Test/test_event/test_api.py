__author__ = 'ar.chusovitin'
import json
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../app/api')
sys.path.append(os.getcwd()+'/../app/route')
import unittest
import requests as rq
from api.event.show_event import filter_by_status
from app.api.service import GameService as gs

URL = 'http://127.0.0.1:13451'
#URL = 'http://87.103.243.110:13451'


class TestEventRoute(unittest.TestCase):

    def test_event_filter_by_status_0(self):
        data = filter_by_status(10, 0)
        self.assertEqual(data[names.ANSWER], names.SUCCESS)
        # Дописать тест, когда поправится задача

    def test_event_filter_by_status_1(self):
        data = filter_by_status(10, 1)
        self.assertEqual(data[names.ANSWER], names.SUCCESS)
        # Дописать тест, когда поправится задача
