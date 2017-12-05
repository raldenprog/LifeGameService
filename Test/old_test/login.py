#for other OS
import json

from api.auth.login_user import login_verification

#for Linux
'''
import sys
import os
directory_user_cabinet= os.getcwd()
directory_user_cabinet=directory_user_cabinet.split("Test")[0]
directory_user_cabinet+="app/api/database"
sys.path.insert(0, directory_user_cabinet)
from login_user import login_verification
'''


def login_done():
    data = {
        'Login': 'test',
        'Password': 'test'
    }
    print(login_verification(data))


def login_error():
    data = {
        # 'login': 'Anton',
        'password': 'qwerty'
    }
    print(login_verification(data))


def login_user():
    file = open('data.data', 'r')
    d = file.readline().split(':')
    file.close()
    data = {
        "Action": "Login",
        "Data": {
            "login": d[0],
            "password": d[1][:-2:]
        }
    }
    return json.dumps(data)
    #print(login_verification(data))

login_done()
"""
login_error()
"""