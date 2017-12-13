# coding: utf8
import logging
import time
from api.database.connect_db import db_connect
from api.sql import SqlQuery

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)

def all_event(count):
    sql = "SELECT Name, Description, Status, Date_start, Date_end FROM Event LIMIT 10 OFFSET {}".format(count)
    try:
        sql = "SELECT Name, Description, Status, Date_start, Date_end FROM Event LIMIT 10 OFFSET {}".format(count)
        if isinstance(count, int) and count >= 0 and count is not None:
            result = SqlQuery(sql)
        else:
            logging.error('Fatal error: execute database')
            return {'Answer': 'Error'}
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def current_event(count):
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_start < {} LIMIT 10 OFFSET {}".format(time.time(), count)
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def end_event(count):
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_end > {} LIMIT 10 OFFSET {}".format(time.time(), count)
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def find_event(alf, count):
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event LIKE '{}%' LIMIT 10 OFFSET {}".format(alf, count)
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def page_event(count):  # Пустышка
    sql = "SELECT Name, Description, Status, Date_start, Date_end FROM Event"
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

def filter_by_status(count, status):
    sql = "SELECT Name, Description, Date_start, Date_end FROM Event where status='{}' LIMIT 10 OFFSET {}".format(status, count)
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'Data': result}

