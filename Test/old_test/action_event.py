#for other OS
from api.event.edit_event import registration_event, update_event

#for Linux
'''
import sys
import os
directory_user_cabinet= os.getcwd()
directory_user_cabinet=directory_user_cabinet.split("Test")[0]
directory_user_cabinet+="app/api/event"
sys.path.insert(0, directory_user_cabinet)
from registration_users import add_user
'''


def registration_done():
    data = {
        names.NAME: 'Anton',
        'description': 'qwerty',
        names.LOGO: '****',
        'status': 'Close',
        'date_start': '12',
        'date_end': '20',
        'date_stop': '13',
        'date_continue': '14'
    }
    print(registration_event(data))


def registration_error():
    data = {
        names.NAME: 'Anton',
        'description': 'qwerty',
        names.LOGO: '****',
        'date_start': '12',
        'date_end': '20',
        'date_stop': '13',
        'date_continue': '14'
    }
    print(registration_event(data))


def update_done():
    data = {
        names.NAME: 'anton',
        'description': 'Qwerty',
        names.LOGO: '****',
        'status': '1',
        'date_start': '12',
        'date_end': '20',
        'date_stop': '13',
        'date_continue': '14'
    }
    print(registration_event(data))


def update_error():
    data = {
        #names.NAME: 'Anton',
        'description': 'qwerty',
        names.LOGO: '****',
        'date_start': '12',
        'date_end': '20',
        'date_stop': '13',
        'date_continue': '14'
    }
    print(registration_event(data))

registration_done()
registration_error()
update_done()
update_error()
