# coding=utf-8
import hashlib
import logging
from api.service import GameService as gs
import api.base_name as names
from api.auth.registration_users import input_session_table

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def get_user_name(id_user):
    """
    Метод возвращает имя пользователя
    :param id_user: int, id пользователя
    :return:
    """
    sql = """Select name from users where id_user = {id_user}""".format(id_user=id_user)
    print(sql)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result[0]}
#print(get_user_name("9"))

def login_verification(user_data):
    """
    Метод проверяет корректность параметров и если всё корректно, передает в метод auth_user
    :param user_data: dict хранит информацию о пользователе
    :return: UUID сессии
    """
    check = [names.LOGIN, names.PASSWORD]
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
        return {names.ANSWER: names.WARNING, names.DATA: user_info}
    #return {names.Answer: 'Ok'}
    return auth_user(user_info)


def auth_user(user_data):
    """
    Метод авторизирует пользователя, присваивая ему UUID сессии
    :param user_data: dict хранит информацию о пользователе
    :return: UUID сессии
    """
    password_hash = hashlib.md5()
    password_hash.update(user_data[names.PASSWORD].encode())
    user_data[names.PASSWORD] = password_hash.hexdigest()
    try:
        sql = "SELECT id_user FROM Auth WHERE Login = '{}' and Password = '{}'".format(user_data[names.LOGIN], user_data[names.PASSWORD])
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: "Ошибка запроса к базе данных"}
    try:
        if len(result) == 0:
            return {names.ANSWER: names.WARNING, names.DATA: "Данного пользователя нет в базе данных"}
    except:
        return {names.ANSWER: names.WARNING, names.DATA: "Логин или пароль не правильные"}
    answer = input_session_table(result[0].get(names.ID_USER))
    if answer.get(names.ANSWER) is not names.SUCCESS:
        return {names.ANSWER: names.WARNING, names.DATA: "Ошибка запроса к базе данных. Неудача"}
    return answer


def logout_user(session):
    """
    Метод закрывает сессию пользователя
    :param session: UUID сессии, которую нужно закрыть
    """
    try:
        sql = "DELETE FROM Session WHERE UUID = '{}'".format(session)
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: "Ошибка запроса к базе данных"}
    try:
        if len(result) == 0:
            return {names.ANSWER: names.WARNING, names.DATA: "Такой сессии нет в базе"}
    except:
        return {names.ANSWER: names.WARNING, names.DATA: "Сессия неверная"}
