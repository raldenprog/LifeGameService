# coding: utf-8
import logging
from api.database.connect_db import db_connect
import decimal
from api.sql import SqlQuery

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def all_users(count):
    # TODO: Добавить в базу users количество очков и добавить это поле в SELECT
    sql = "SELECT Name, id_user FROM Users LIMIT 10 OFFSET {}".format(count)
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}


def event_users(count, event):
    # TODO: Добавить в базу users количество очков и добавить это поле в SELECT
    # TODO: Добавить условие WHERE для фильтрации по event'ам
    sql = "SELECT Name, id_user FROM Users WHERE id_event={} LIMIT 10 OFFSET {}".format(event, count)
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}


def get_scoreboard():
    #TODO: Временное решение. Номер события
    id_event = 2
    sql = """select T2.Login, T2.point from
  (
    select a.Login as Login, sum(point) as point, max(b.time) as user_time
   from Auth a, task_acc b
   where a.id_user = b.id_user and b.id_event = {}
    GROUP BY a.Login
  ) as T2
where point is not NULL
order by point desc, user_time desc;""".format(id_event)
    print(sql)
    try:
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}
