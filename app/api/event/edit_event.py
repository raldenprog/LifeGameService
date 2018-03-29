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
    check = [names.NAME, 'Description', names.LOGO,
             'Status', 'Date_start', 'Date_end',
             'Date_stop', 'Date_continue']
    registration_data = {names.NAME: '', 'Description': '', names.LOGO: '',
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
        return {names.ANSWER: names.ERROR, names.DATA: registration_data}
    return input_event_table(registration_data)


def input_event_table(event_data):
    """
    Метод добавляет запись в таблицу "События"
    :param event_data: dict информация о событии
    :return: {names.ANSWER: ответ}
    """
    try:
        sql = """INSERT INTO event ("name", description, logo, status, date_start, date_end, date_stop, date_continue) 
VALUES (\'{Name}\', \'{Description}\', 
\'{Logo}\', \'{Status}\', \'{Date_start}\', \'{Date_end}\', 
\'{Date_stop}\', \'{Date_continue}\')""".format(**event_data)
        print(sql)
        gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}

    return {names.ANSWER: names.SUCCESS}


def update_event(event_data):
    """
    Метод обновляет данные о событии
    :param event_data: dict информация о событии
    :return: {names.ANSWER: ответ}
    """
    check = [names.ID_EVENT, names.NAME, 'Description', names.LOGO,
             'Status', 'Date_start', 'Date_end',
             'Date_stop', 'Date_continue']
    update_data = {names.ID_EVENT: '', names.NAME: '', 'Description': '', names.LOGO: '',
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
        return {names.ANSWER: names.ERROR, names.DATA: update_data}
    return update_event_table(update_data)


def update_event_table(user_data):
    """
    Метод обновляет запись в таблице "События"
    :param user_data: dict информация о событии
    :return: {names.ANSWER: ответ}
    """
    try:
        sql = """UPDATE event 
SET Name='{Name}', Description='{Description}', Logo='{Logo}', 
Status='{Status}', Date_start='{Date_start}', Date_end='{Date_end}', 
Date_stop='{Date_stop}', Date_continue='{Date_continue}' WHERE id_event='{id_event}'""".format(**user_data)
        gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS}


def delete_event(user_data):
    pass


def update_status_event():
    update_status_close_events()
    update_status_open_events()


def update_status_close_events():
    """
    Метод закрывает событие, если оно закончилось либо закрыто на перерыв
    :return:
    """
    sql = """update event
    set status = 0
    where CURRENT_TIMESTAMP >= date_end
    or (CURRENT_TIMESTAMP >= date_stop and CURRENT_TIMESTAMP < date_continue)
    and status = 1
    """
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def update_status_open_events():
    """
    Метод запускает событие, если оно началось либо закончился перерыв
    :return:
    """
    sql = """update event
    set status = 1
    where (CURRENT_TIMESTAMP >= date_start and CURRENT_TIMESTAMP < date_stop)
    or (CURRENT_TIMESTAMP >= date_continue and CURRENT_TIMESTAMP < date_end)
    and status = 0
    """
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}