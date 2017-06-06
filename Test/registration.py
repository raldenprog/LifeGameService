#for other OS
from app.api.database.registration_users import add_user

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


registration_done()
registration_error()
