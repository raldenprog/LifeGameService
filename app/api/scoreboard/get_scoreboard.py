# coding: utf-8
import logging
import time
from app.api.database.connect_db import db_connect

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)

def all_users(count):
    connect, current_connect = db_connect()
    # TODO: Добавить в базу users количество очков и добавить это поле в SELECT
    sql = "SELECT Name, ID FROM Users LIMIT 10 OFFSET {}".format(count)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}

def event_users(count, event):
    connect, current_connect = db_connect()
    # TODO: Добавить в базу users количество очков и добавить это поле в SELECT
    # TODO: Добавить условие WHERE для фильтрации по event'ам
    sql = "SELECT Name, ID FROM Users WHERE event={} LIMIT 10 OFFSET {}".format(event, count)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}
