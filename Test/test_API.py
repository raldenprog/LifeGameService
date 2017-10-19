# coding=utf-8
import json
import unittest
import requests as req
from random import choice
from string import ascii_lowercase

URL = "http://127.0.0.1:13451"
#URL = "http://87.103.243.110:13451"


class TestRegistration(unittest.TestCase):
    def test_registration(self):
        data = json.dumps({
            'Login': 'anton',#.join(choice(ascii_lowercase) for i in range(12)),
            'Password': '2',
            'Name': '3',
            'Surname': '4',
            'Email': 'a@a.ru',
            'Sex': '5',
            'City': '6',
            'Educational': '7',
            'Logo_name': '8',
            'Logo': '9'
        })
        data = req.request('POST', '%s/registration' % URL, data={'Data': data})
        print('registration')
        print(data.text)
        print(data)
        print(data.headers)

    def test_auth(self):
        data = json.dumps({
            'Login': 'anton',
            'Password': '2'
        })
        data = req.request('POST', '%s/auth' % URL, data={'Data': data})
        print('auth')
        print(data.text)
        print(data)
        print(data.headers)