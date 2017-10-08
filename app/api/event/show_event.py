import logging
import time
from api.database.connect_db import db_connect

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)

def all_event(count):
    connect, current_connect = db_connect()
    sql = "SELECT Name, Description, Status, Date_start, Date_end FROM Event LIMIT 10 OFFSET {}".format(count)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def current_event(count):
    connect, current_connect = db_connect()
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_start < {} LIMIT 10 OFFSET {}".format(time.time(), count)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def end_event(count):
    connect, current_connect = db_connect()
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_end > {} LIMIT 10 OFFSET {}".format(time.time(), count)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def find_event(alf, count):
    connect, current_connect = db_connect()
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event LIKE '{}%' LIMIT 10 OFFSET {}".format(alf, count)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def page_event(count):  # Пустышка
    connect, current_connect = db_connect()
    sql = "SELECT Name, Description, Status, Date_start, Date_end FROM Event"
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}
