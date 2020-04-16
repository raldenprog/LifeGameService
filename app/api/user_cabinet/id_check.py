# coding: utf8
import logging
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def check_id(id_user):
    """
    Передаем функции искомый id.
    Возвращает True если id есть, False если id нет
    """
    sql = "select exists(select 1 from users where id_user = {})".format(id_user)
    return gs.SqlQuery(sql).get('exists', False)