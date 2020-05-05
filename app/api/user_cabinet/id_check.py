# coding: utf8
from api.service import GameService as gs


def check_id(id_user):
    """
    Передаем функции искомый id.
    Возвращает True если id есть, False если id нет
    """
    sql = "select exists(select 1 from users where id_user = {})".format(id_user)
    return gs.SqlQuery(sql).get('exists', False)