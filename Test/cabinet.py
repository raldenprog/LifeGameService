#for other OS
from app.api.user_cabinet.cabinet import user_cabinet, change_password, edit_cabinet
from app.api.database.connect_db import db_connect

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


def check_edit_cabinet():
    data = {"id": "1",
            "name": "Value",
            "patronymic": "Value",
            "email": "Value",
            "sex": "Value",
            "city": "Value",
            "Educational": "Value",
            "logo": "Value"
            }
    answer = edit_cabinet(data)
    if answer["Answer"]=='Success':
        connect, current_connect = db_connect()
        current_connect.execute("SELECT name, patronymic, email, sex, city, Educational, logo FROM users where id = '{}'".format(
           data['id']
          ))
        result = current_connect.fetchall()[0]
        flag=0
        for i in result:
            if result[i] != "Value":
                flag=1
                print ("Error")
        if flag == 0:
            print ("Ok")
        data = {"id": "1",
                "name": "Value1",
                "patronymic": "Value2",
                "email": "Value3",
                "sex": "Value4",
                "city": "Value5",
                "Educational": "Value6",
                "logo": "Value7"
                }
        edit_cabinet(data)


cabinet_done()
cabinet_error()
check_change_password()
check_edit_cabinet()