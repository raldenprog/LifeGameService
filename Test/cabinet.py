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
        "id": "1"
    }
    print (user_cabinet(data))


def cabinet_error():
    data = {
        'login': 'Anton'
    }
    print(user_cabinet(data))


def check_change_password():
    data = {"id": "3",
            "old_password": "qwerty",
            "new_password": "pinlox123"
            }
    check = change_password(data)
    if check['Answer'] == 'Success':
        data = {"id": "3",
                "old_password": "pinlox123",
                "new_password": "qwerty"
                }
        check = change_password(data)
        if check['Answer'] == 'Success':
            print("Ok")
        else:
            print("Error")
    else:
        print("Error")

cabinet_done()
cabinet_error()
check_change_password()
