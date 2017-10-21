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
        return {"Answer": "Warning"}
    try:
        sql = "SELECT User FROM Session WHERE UUID = '{}'".format(session)
        print(sql)
        current_connect.execute(sql)
        connect.commit()
    except:
        logging.error('Fatal error: execute database')
        return {"Answer": "Ошибка запроса к базе данных"}
    result = current_connect.fetchone()
    try:
        if len(result) == 0:
            return {'Answer': 'Warning', "Data": "Такой сессии нет в базе"}
    except:
        return {'Answer': 'Warning', "Data": "Сессия неверная"}
    return result['User']