#for other OS
from app.api.database.login_user import login_verification

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
        'login': 'Anton',
        'password': 'qwerty'
    }
    print(login_verification(data))


def login_error():
    data = {
        # 'login': 'Anton',
        'password': 'qwerty'
    }
    print(login_verification(data))


login_done()
login_error()
