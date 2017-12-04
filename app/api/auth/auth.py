import logging
from api.sql import SqlQuery
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def session_verification(session):
    """
    Возвращает ID пользователя к которому привязан UUID
    :param session: 
    :return: 
    """
    try:
        sql = "SELECT User FROM Session WHERE UUID = '{}'".format(session)
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return None
    try:
        if len(result) == 0:
            return None
    except:
        return None
    return result['User']


def get_login(id_user):
    """
    Возвращает Login пользователя 
    :param session: 
    :return: 
    """
    try:
        sql = "SELECT Login FROM Auth WHERE User = '{}'".format(id_user)
        result = SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return None
    try:
        if len(result) == 0:
            return None
    except:
        return None
    return result['Login']