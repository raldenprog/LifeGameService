# coding: utf-8
import logging
import time
from api.database.connect_db import db_connect
import decimal

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


def get_scoreboard():
    #TODO: Временное решение. Номер события
    id_event = 1
    connect, current_connect = db_connect()
    sql = """select T2.Login, T2.point from
  (
    select a.Login as Login, sum(point) as point, max(b.time) as user_time
   from Auth a, task_acc b
   where a.User = b.id_user and b.id_event = {}
    GROUP BY a.Login
  ) as T2
where point is not NULL
order by point desc, user_time desc;""".format(id_event)
    print(sql)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    for i in result:
        if issubclass(i['point'].__class__, decimal.Decimal):
            i['point'] = int(i.get('point'))
        else:
            i['point'] = 0
    return {'Answer': 'Success', 'data': result}
