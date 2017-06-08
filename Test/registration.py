#for other OS
from app.api.database.registration_users import add_user
import random
import string
import json
#for Linux
'''
import sys
import os
directory_user_cabinet= os.getcwd()
directory_user_cabinet=directory_user_cabinet.split("Test")[0]
directory_user_cabinet+="app/api/database"
sys.path.insert(0, directory_user_cabinet)
from registration_users import add_user
'''


def registration_done():
    data = {
        'login': 'Anton',
        'password': 'qwerty',
        'name': 'anton123',
        'patronymic': 'ch',
        'email': 'a@a.ru',
        'sex': 'male',
        'city': 'Nsk',
        'Educational': 'Sibsutis',
        'logo_name': '1',
        'logo': 'logooo'
    }
    print(add_user(data))


def registration_error():
    data = {
        # 'login': 'Anton',
        'password': 'qwerty',
        'name': 'anton123',
        'patronymic': 'ch',
        'email': 'a@a.ru',
        'sex': 'male',
        'city': 'Nsk',
        'Educational': 'Sibsutis',
        'logo_name': '1',
        'logo': 'logooo'
    }
    print(add_user(data))


def registration_user_data():
    a = string.ascii_lowercase+string.ascii_uppercase+string.digits
    login = ''.join(random.choice(a) for i in range(random.randint(5, 30)))
    password = ''.join(random.choice(a) for i in range(random.randint(5, 30)))
    name = ''.join(random.choice(a) for i in range(random.randint(5, 30)))
    patronymic = ''.join(random.choice(a) for i in range(random.randint(5, 30)))
    email = ''.join(random.choice(a) for i in range(random.randint(5, 10)))+'@' + \
            ''.join(random.choice(a) for i in range(random.randint(5, 10)))+'.' + \
            ''.join(random.choice(a) for i in range(random.randint(5, 10)))

    file = open('data.data', 'a')
    file.write(login+':'+password+'\n')
    file.close()
    data = {
        "Action": "Registration",
        "Data": {
            'login': login,
            'password': password,
            'name': name,
            'patronymic': patronymic,
            'email': email,
            'sex': 'male',
            'city': 'Nsk',
            'Educational': 'Sibsutis',
            'logo_name': '1',
            'logo': 'logooo'
        }
    }
    return json.dumps(data)
    #print(add_user(data))

"""
registration_done()
registration_error()
"""
