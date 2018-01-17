#for other OS
import json
import random
import string

from api.auth.registration_users import registration_user

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
        names.LOGIN: 'Anton451241',
        names.PASSWORD: 'qwerty',
        names.NAME: 'anton123',
        names.SURNAME: 'ch',
        names.EMAIL: 'a@a.ru',
        names.SEX: 'male',
        names.CITY: 'Nsk',
        names.EDUCATION: 'Sibsutis',
        names.LOGO_NAME: '1',
        names.LOGO: 'logooo'
    }
    registration_user(data)


def registration_error():
    data = {
        # names.LOGIN: 'Anton',
        names.PASSWORD: 'qwerty',
        names.NAME: 'anton123',
        'patronymic': 'ch',
        names.EMAIL: 'a@a.ru',
        names.SEX: 'male',
        names.CITY: 'Nsk',
        names.EDUCATION: 'Sibsutis',
        names.LOGO_NAME: '1',
        names.LOGO: 'logooo'
    }
    #print(registration_user(data))


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
        names.DATA: {
            names.LOGIN: login,
            names.PASSWORD: password,
            names.NAME: name,
            'patronymic': patronymic,
            names.EMAIL: email,
            names.SEX: 'male',
            names.CITY: 'Nsk',
            names.EDUCATION: 'Sibsutis',
            names.LOGO_NAME: '1',
            names.LOGO: 'logooo'
        }
    }
    return json.dumps(data)
    #print(add_user(data))


registration_done()
registration_error()

