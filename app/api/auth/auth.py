from api.service import GameService as gs
import api.base_name as names


def session_verification(session):
    """
    Метод проверяет, существует ли пользовательская сессия
    :param session: UUID сессии
    :return: int Возвращает ID пользователя
    """
    #try:
    sql = "SELECT id_user FROM Session WHERE UUID = '{}'".format(session)
        #print(sql)
    result = gs.SqlQuery(sql)
    #except:
    #    return None
    #try:
    #    if len(result) == 0:
    #        return None
    #except:
     #   return None
    return result[0]["id_user"]


def get_login(id_user):
    """
    Метод получает логин по ID пользователя
    :param id_user: ID пользователя
    :return: str Логин пользователя
    """
    sql = "SELECT Login FROM Auth WHERE User = '{}'".format(id_user)
    result = gs.SqlQuery(sql)
    if len(result) == 0:
        return None
    return result[names.LOGIN]
