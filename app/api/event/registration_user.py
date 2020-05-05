__author__ = 'RaldenProg'
from api.service import GameService as gs
import api.base_name as names


def check_registration(data):
    """
    Метод проверки, зарегестрирован ли пользователь на данное событие
    :param data: dict: id_user, id_event
    :return: True or False
    """
    sql = "SELECT id_user FROM participation WHERE id_user=\'{id_user}\' and id_event=\'{id_event}\'".format(**data)
    #print(sql)
    answer = gs.SqlQuery(sql)
    if answer == []:
        return True
    else:
        return False

def check_event(data):
    """
        Метод проверяет существует ли событие
        :param data: dict: id_event
        :return: True or False
        """
    sql = "SELECT name FROM event WHERE id_event=\'{id_event}\'".format(**data)
    print(sql)
    answer = gs.SqlQuery(sql)
    if answer != []:
        return True
    else:
        return False

def registration(data):
    """
    Метод регистрирует пользователя на событие
    :param data: dict: id_user, id_event
    :return: {names.ANSWER: ответ}
    """
    if check_registration(data):
        if check_event(data):
            sql = "INSERT INTO participation (id_user, id_event) VALUES (\'{id_user}\', \'{id_event}\')".format(**data)
            #print(sql)
            gs.SqlQuery(sql)
        else:
            return {names.ANSWER: "Event not found"}
    else:
        return {names.ANSWER: "User already registered"}

    return {names.ANSWER: names.SUCCESS}
