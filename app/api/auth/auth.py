import logging
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def session_verification(session):
    """
    Метод проверяет, существует ли пользовательская сессия
    :param session: UUID сессии
    :return: int Возвращает ID пользователя
    """
    try:
        sql = "SELECT id_user FROM Session WHERE UUID = '{}'".format(session)
        #print(sql)
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return None
    try:
        if len(result) == 0:
            return None
    except:
        return None
    return result[0]["id_user"]


def get_login(id_user):
    """
    Метод получает логин по ID пользователя
    :param id_user: ID пользователя
    :return: str Логин пользователя
    """
    try:
        sql = "SELECT Login FROM Auth WHERE User = '{}'".format(id_user)
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return None
    try:
        if len(result) == 0:
            return None
    except:
        return None
    return result[names.LOGIN]
