#for other OS
from api.user_cabinet.cabinet import user_cabinet, change_password

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
        names.ID: "1"
    }
    print (user_cabinet(data))


def cabinet_error():
    data = {
        names.LOGIN: 'Anton'
    }
    print(user_cabinet(data))


def check_change_password():
    data = {names.ID: "3",
            "old_password": "qwerty",
            "new_password": "pinlox123"
            }
    check = change_password(data)
    if check[names.ANSWER] == names.SUCCESS:
        data = {names.ID: "3",
                "old_password": "pinlox123",
                "new_password": "qwerty"
                }
        check = change_password(data)
        if check[names.ANSWER] == names.SUCCESS:
            print("Ok")
        else:
            print(names.ERROR)
    else:
        print(names.ERROR)

cabinet_done()
cabinet_error()
check_change_password()
