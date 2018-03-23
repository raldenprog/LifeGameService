__author__ = 'RaldenProg'

import logging
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def check_registration(data):
    """
    Метод проверки, зарегестрирован ли пользователь на данное событие
    :param data: dict: id_user, id_event
    :return: {names.ANSWER: ответ}
    """
    try:
        sql = "SELECT id_user FROM participation WHERE id_user=\'{id_user}\' and id_event=\'{id_event}\'".format(**data)
        #print(sql)
        answer = gs.SqlQuery(sql)
        if answer == []:
            return True
        else:
            return False
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return False

def check_event(data):
    try:
        sql = "SELECT name FROM event WHERE id_event=\'{id_event}\'".format(**data)
        #print(sql)
        answer = gs.SqlQuery(sql)
        if answer != []:
            return True
        else:
            return False
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return False

def registration(data):
    """
    Метод регистрирует пользователя на событие
    :param data: dict: id_user, id_event
    :return: {names.ANSWER: ответ}
    """
    try:
        if check_registration(data):
            if check_event(data):
                sql = "INSERT INTO participation (id_user, id_event) VALUES (\'{id_user}\', \'{id_event}\')".format(**data)
                #print(sql)
                gs.SqlQuery(sql)
            else:
                return {names.ANSWER: "event not found"}
        else:
            return {names.ANSWER: "User already registered"}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}

    return {names.ANSWER: names.SUCCESS}
