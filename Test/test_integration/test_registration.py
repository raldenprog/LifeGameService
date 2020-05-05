#!/usr/bin/env python3.6
# coding=utf-8
import requests as req
import unittest
from app.api.config import DATABASE


class TestRegistration(unittest.TestCase):
    def test_registration(self):
        data = req.request('POST', f'''{DATABASE.get('host')}/registration''')
        print(data.text)
        print(data)
        print(data.headers)