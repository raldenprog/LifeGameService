#for other OS
from app.api.user_cabinet.cabinet import user_cabinet

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
    print(user_cabinet(data))


def cabinet_error():
    data = {
        'login': 'Anton'
    }
    print(user_cabinet(data))


cabinet_done()
cabinet_error()
