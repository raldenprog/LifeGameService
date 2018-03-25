# coding: utf8
import logging
import time
import datetime
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def info_event(id_event):
    """
    Метод возвращает название события
    :param id_event: int, id события
    :return:
    """
    sql = """Select name from event where id_event = {id_event}""".format(id_event=id_event)
    #print(sql)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result[0]}


def all_event(id_user, count):
    """
    Метод возвращает 10 событий, начиная с заданного номера
    :param id_user: int id пользователя
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    try:
        sql = """with 
events as (
  select id_event
  , Name
  , Status
  , Date_start
  , Date_end
  , case when (Date_end - Date_start) < interval '0 hours' then null else timestamp '2001-01-01 00:00' + (Date_end - Date_start) - interval '2001 year' end::text as interval
  , case when (select 1 from participation where id_user =  {id_user} and id_event = ev.id_event) is not null then True else False end as participation
  , (select count(*) from participation where id_event = ev.id_event) as count
  from Event ev
  order by status desc, date_start, date_end
  limit 10
  offset {count}
)
table events""".format(count=count, id_user=id_user)
        print(sql)
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
            print(result)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def current_event(count):
    """
    Метод возвращает 10 событий, начиная с заданного номера и если они еще не начались
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_start < {} LIMIT 10 OFFSET {}".format(time.time(), count)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def end_event(count):
    """
    Метод возвращает 10 событий, начиная с заданного номера и если они закончились
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_end > {} LIMIT 10 OFFSET {}".format(datetime.datetime.now().strftime('%d.%m.%Y'), count)
    print(sql)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}

def find_event(alf, count):

    """
    Метод возвращает 10 событий, начиная с заданного номера и если они закончились
    :param alf: str Символы, которые встречаются в названии события
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT id_event, Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Name LIKE '%{}%' ORDER BY id_event LIMIT 10 OFFSET {}".format(alf, count)
    #print(sql)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
            #print(result)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def page_event(data):
    sql = "SELECT Name, Description, logo, Date_start, Date_end, Date_continue, Status FROM event WHERE id_event = {}".format(data["id_event"])
    try:
        if isinstance(data["id_event"], int):
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}

def filter_by_status(count, status):
    """
    Метод возвращает 10 событий, начиная с заданного номера и если они закончились
    :param count: int номер события, с которого начинать вывод
    :param status: int Признак завершенного или активного события
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT Name, Description, Date_start, Date_end FROM Event where status='{}' LIMIT 10 OFFSET {}".format(status, count)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}
