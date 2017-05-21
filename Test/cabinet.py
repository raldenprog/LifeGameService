#for other OS
from app.api.user_cabinet.cabinet import user_cabinet, change_password

#for Linux
'''
import sys
import os
directory_user_cabinet= os.getcwd()
directory_user_cabinet=directory_user_cabinet.split("Test")[0]
directory_user_cabinet+="app/api/user_cabinet"
sys.path.insert(0, directory_user_cabinet)
from cabinet import user_cabinet
'''


def cabinet_done():
    data = {
        "id": "2"
    }
    user_cabinet(data)


def cabinet_error():
    data = {
        'login': 'Anton'
    }
    print(user_cabinet(data))


def check_change_password():
    data = {"id": "1",
            "login": "Value",
            "old_password": "pinlox123",
            "new_password": "qwerty"
            }
    print (change_password(data))

cabinet_done()
#cabinet_error()
#check_change_password()