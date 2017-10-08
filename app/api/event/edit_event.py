# coding: utf8
import logging
from api.database.connect_db import db_connect


logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def registration_event(user_data):
    check = ['Name', 'Description', 'Logo',
             'Status', 'Date_start', 'Date_end',
             'Date_stop', 'Date_continue']
    registration_data = {'Name': '', 'Description': '', 'Logo': '',
        'Status': '', 'Date_start': '', 'Date_end': '',
        'Date_stop': '', 'Date_continue': ''}
    flag = False
    for data in check:
        try:
            if user_data[data] is None:
                logging.info('Incorrect parameter ' + data)
                registration_data[data] = 'Error'
                flag = True
            else:
                registration_data[data] = user_data[data]
        except:
            logging.error('Fatal error: param ' + data)
            registration_data[data] = 'Error'
            flag = True
    if flag:
        return {"Answer": "Error", 'Data': registration_data}
    return input_event_table(registration_data)


def input_event_table(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Error"}
    try:
        sql = "INSERT INTO event VALUES (null, \"{Name}\", \"{Description}\", \"{Logo}\", \"{Status}\", {Date_start}, {Date_end}, {Date_stop}, {Date_continue})".format(**user_data)
        current_connect.execute(sql)
        connect.commit()
        connect.close()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}

    return {'Answer': 'Success'}


def update_event(user_data):
    check = ['ID', 'Name', 'Description', 'Logo',
             'Status', 'Date_start', 'Date_end',
             'Date_stop', 'Date_continue']
    update_data = {'ID': '', 'Name': '', 'Description': '', 'Logo': '',
        'Status': '', 'Date_start': '', 'Date_end': '',
        'Date_stop': '', 'Date_continue': ''}
    flag = False
    for data in check:
        try:
            if user_data[data] is None:
                logging.info('Incorrect parameter ' + data)
                update_data[data] = 'Error'
                flag = True
            else:
                update_data[data] = user_data[data]
        except:
            logging.error('Fatal error: param ' + data)
            update_data[data] = 'Error'
            flag = True
    if flag:
        return {"Answer": "Error", 'Data': update_data}
    return update_event_table(update_data)

def update_event_table(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Error"}
    try:
        sql = "UPDATE event SET Name='{Name}', Description='{Description}', Logo='{Logo}', Status='{Status}', Date_start='{Date_start}', Date_end='{Date_end}', Date_stop='{Date_stop}', Date_continue='{Date_continue}' WHERE ID='{ID}'".format(**user_data)
        current_connect.execute(sql)
        connect.commit()
        connect.close()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success'}


def delete_event(user_data):
    pass
