# coding: utf8
import logging
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def registration_event(event_data):
    """
    Метод регистрирует событие
    :param event_data: dict информация о событии
    :return: {names.ANSWER: ответ}
    """
    check = ['Name', 'Description', 'Logo',
             'Status', 'Date_start', 'Date_end',
             'Date_stop', 'Date_continue']
    registration_data = {'Name': '', 'Description': '', 'Logo': '',
        'Status': '', 'Date_start': '', 'Date_end': '',
        'Date_stop': '', 'Date_continue': ''}
    flag = False
    for data in check:
        try:
            if event_data[data] is None:
                logging.info('Incorrect parameter ' + data)
                registration_data[data] = names.ERROR
                flag = True
            else:
                registration_data[data] = event_data[data]
        except:
            logging.error('Fatal error: param ' + data)
            registration_data[data] = names.ERROR
            flag = True
    if flag:
        return {names.ANSWER: names.ERROR, 'Data': registration_data}
    return input_event_table(registration_data)


def input_event_table(event_data):
    """
    Метод добавляет запись в таблицу "События"
    :param event_data: dict информация о событии
    :return: {names.ANSWER: ответ}
    """
    try:
        sql = """INSERT INTO id_event 
VALUES (null, \"{Name}\", \"{Description}\", 
\"{Logo}\", \"{Status}\", {Date_start}, {Date_end}, 
{Date_stop}, {Date_continue})""".format(**event_data)
        gs.SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {names.ANSWER: names.ERROR}

    return {names.ANSWER: 'Success'}


def update_event(event_data):
    """
    Метод обновляет данные о событии
    :param event_data: dict информация о событии
    :return: {names.ANSWER: ответ}
    """
    check = ['ID', 'Name', 'Description', 'Logo',
             'Status', 'Date_start', 'Date_end',
             'Date_stop', 'Date_continue']
    update_data = {'ID': '', 'Name': '', 'Description': '', 'Logo': '',
        'Status': '', 'Date_start': '', 'Date_end': '',
        'Date_stop': '', 'Date_continue': ''}
    flag = False
    for data in check:
        try:
            if event_data[data] is None:
                logging.info('Incorrect parameter ' + data)
                update_data[data] = names.ERROR
                flag = True
            else:
                update_data[data] = event_data[data]
        except:
            logging.error('Fatal error: param ' + data)
            update_data[data] = names.ERROR
            flag = True
    if flag:
        return {names.ANSWER: names.ERROR, 'Data': update_data}
    return update_event_table(update_data)


def update_event_table(user_data):
    """
    Метод обновляет запись в таблице "События"
    :param user_data: dict информация о событии
    :return: {names.ANSWER: ответ}
    """
    try:
        sql = """UPDATE id_event 
SET Name='{Name}', Description='{Description}', Logo='{Logo}', 
Status='{Status}', Date_start='{Date_start}', Date_end='{Date_end}', 
Date_stop='{Date_stop}', Date_continue='{Date_continue}' WHERE ID='{ID}'""".format(**user_data)
        gs.SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: 'Success'}


def delete_event(user_data):
    pass
