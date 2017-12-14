# coding: utf8
import logging
from api.sql import SqlQuery

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def check_id(id_user):
    """
    Передаем функции искомый id.
    Возвращает 1 если id есть, 0 если id нет
    """
    try:
        sql = "select exists(select 1 from users where id_user = {})".format(id_user)
        return SqlQuery(sql)[0].get('exists', False)
    except:
        logging.error('Fatal error: check id')
        return {"Answer": "Error"}