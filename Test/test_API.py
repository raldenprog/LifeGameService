# coding=utf-8
import json
import unittest
import requests as req
import api.task.tasks as tasks
import api.auth.auth as auth
from random import choice
from string import ascii_lowercase

URL = 'http://127.0.0.1:13451'
# URL = 'http://87.103.243.110:13451'


class TestRegistration(unittest.TestCase):

    @unittest.skip
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

    @unittest.skip
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

    @unittest.skip
    def test_create_task(self):
        data = [{
            'task_category': 'ppc',
            'task_name': 'Task1',
            'task_flag': 'flag{flagflag}',
            'task_description': 'Тестовое описание',
            'task_point': 100,
            'task_hint': '',
            'task_link': ''
            }, {
            'task_category': 'stego',
            'task_name': 'Task2',
            'task_flag': 'flag{flag1flag1}',
            'task_description': 'Тестовое описание stego задания',
            'task_point': 200,
            'task_hint': 'Подсказка здесь',
            'task_link': ''
            }, {
            'task_category': 'ppc',
            'task_name': 'Task3',
            'task_flag': 'flag{flag1flag2}',
            'task_description': 'Тестовое описание ppc2 задания',
            'task_point': 250,
            'task_hint': '',
            'task_link': 'http://www.google.com'
            }]
        for task in data:
            print(tasks.create_one_task(task))

    def test_get_task(self):
        data = {
            'id_event': 1,
            'id_user': 1
        }
        data = tasks.get_task_event(data)
        print(data)

    @unittest.skip
    def test_session(self):
        data = json.dumps({
            'Login': 'anton',
            'Password': '2'
        })
        #data = req.request('POST', '%s/auth' % URL, data={'Data': data})
        data = 'c2f57e8d-bb8a-43c7-aeac-339dc311de71'
        print(data)
        print(auth.session_verification(data))

    @unittest.skip
    def test_check_task(self):
        data = {
            'Task_name': 'Task3',
            'Task_flag': 'flag{flag1flag2}'
        }
        print(tasks.check_task(data))
