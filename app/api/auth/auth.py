import hashlib
import logging
from api.database.connect_db import db_connect
from api.auth.registration_users import input_session_table

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def session_verification(session):
    """
    Возвращает ID пользователя к которому привязан UUID
    :param session: 
    :return: 
    """
    connect, current_connect = db_connect()
    if connect == -1:
        return None
    try:
        sql = "SELECT User FROM Session WHERE UUID = '{}'".format(session)
        print(sql)
        current_connect.execute(sql)
        connect.commit()
    except:
        logging.error('Fatal error: execute database')
        return None
    result = current_connect.fetchone()
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
    connect, current_connect = db_connect()
    if connect == -1:
        return None
    try:
        sql = "SELECT Login FROM Auth WHERE User = '{}'".format(id_user)
        print(sql)
        current_connect.execute(sql)
        connect.commit()
    except:
        logging.error('Fatal error: execute database')
        return None
    result = current_connect.fetchone()
    try:
        if len(result) == 0:
            return None
    except:
        return None
    return result['Login']