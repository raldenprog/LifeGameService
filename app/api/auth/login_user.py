# coding=utf-8
import hashlib
import logging
from api.database.connect_db import db_connect
from api.auth.registration_users import input_session_table

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def login_verification(user_data):
    check = ['Login', 'Password']
    user_info = dict.fromkeys(check, '')
    error = False
    for data in check:
        if user_data.get(data, None) is None:
            logging.info('Incorrect parameter ' + data)
            user_info[data] = 'Пустой параметр!'
            error = True
        else:
            user_info[data] = user_data[data]
    if error:
        return {"Answer": "Warning", 'Data': user_info}
    #return {'Answer': 'Ok'}
    return auth_user(user_info)


def auth_user(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Warning"}
    # TODO: Необходимо делать на стороне фронта
    password_hash = hashlib.md5()
    password_hash.update(user_data['Password'].encode())
    user_data['Password'] = password_hash.hexdigest()
    try:
        sql = "SELECT User FROM Auth WHERE Login = '{}' and Password = '{}'"
        print(sql.format(user_data['Login'], user_data['Password']))
        current_connect.execute(sql.format(user_data['Login'], user_data['Password']))
        connect.commit()
    except:
        logging.error('Fatal error: execute database')
        return {"Answer": "Ошибка запроса к базе данных"}
    result = current_connect.fetchone()
    try:
        if len(result) == 0:
            return {'Answer': 'Warning', "Data": "Данного пользователя нет в базе данных"}
    except:
        return {'Answer': 'Warning', "Data": "Логин или пароль не правильные"}
    answer = input_session_table(result.get('User'), connect, current_connect)
    if answer.get('Answer') is not "Success":
        return {'Answer': 'Warning', "Data": "Ошибка запроса к базе данных. Неудача"}
    return answer


def logout_user(session):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Warning"}
    try:
        sql = "DELETE FROM Session WHERE UUID = '{}'".format(session)
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