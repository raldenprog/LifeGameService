# coding=utf-8
import hashlib
import logging
import uuid
# Временно нужно оставить, отдельную задачу на переделывания регистрации
from api.database.connect_db import db_connect_new
from api.service import GameService as gs
import api.base_name as names

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def registration_user(user_data):
    """
    Метод проверяет корректность введенных данных
    :param user_data: dict данные пользователя
    :return: UUID сессии
    """
    check = [names.LOGIN, names.PASSWORD, names.NAME, names.EMAIL, names.SEX,
             names.CITY, names.EDUCATION, names.LOGO_NAME, names.LOGO]
    registration_data = dict.fromkeys(check, '')
    error = False
    for data in check:
        if user_data.get(data, None) is None:
            logging.info('Incorrect parameter ' + data)
            registration_data[data] = 'Пустой параметр!'
            error = True
        else:
            registration_data[data] = user_data[data]
    if error:
        return {names.ANSWER: names.ERROR, names.DATA: registration_data}
    # TODO: Загрузить логотип в файл
    """
    with open('../app/resources/logo_users/{}'.format(user_data.get(names.LOGO_NAME)), 'wb') as logo_file:
        logo_file.write(user_data[names.LOGO])
        registration_data[names.LOGO] = 'True'
    """
    answer = input_auth_table(registration_data)
    if answer.get(names.ANSWER) is not names.SUCCESS:
        return {names.ANSWER: names.WARNING, names.DATA: "Ошибка запроса к базе данных"}
    return answer


def input_auth_table(user_data):
    """
    Метод начинает цепочку регистрации в бд
    Заносится изменение в таблицу auth
    :param user_data: dict данные пользователя
    :return: UUID сессии
    """
    connect, current_connect = db_connect_new()
    if connect == -1:
        return {names.ANSWER: names.WARNING, names.DATA: "Ошибка доступа к базе данных, повторить позже"}
    password_hash = hashlib.md5()
    password_hash.update(user_data[names.PASSWORD].encode())
    user_data[names.PASSWORD] = password_hash.hexdigest()
    sql = "INSERT INTO Auth (login, password)" \
          " VALUES (\'{Login}\',\'{Password}\') RETURNING id_user".format(
        Login=user_data.get(names.LOGIN),
        Password=user_data.get(names.PASSWORD))
    id_user = gs.SqlQuery(sql)[0]['id_user']
    return input_access_table(id_user, user_data, connect, current_connect)


def input_access_table(id_user, user_data, connect, current_connect):
    """
    Промежуточный метод, заносит данные в таблицу "Права доступа"
    :param id_user: int ID пользователя
    :param user_data: dict Данные пользователя
    :param connect: соединение с бд
    :param current_connect: соединение с бд
    :return: UUID сессии
    """
    sql = "INSERT INTO Access" \
          " VALUES ({id},0)".format(id=id_user)
    gs.SqlQuery(sql)
    return input_user_table(id_user, user_data, connect, current_connect)


def input_user_table(id_user, user_data, connect, current_connect):
    """
    Промежуточный метод, добавляет данные в таблицу "Информация о пользователе"
    :param id_user: int ID пользователя
    :param user_data: dict Данные пользователя
    :param connect: соединение с бд
    :param current_connect: соединение с бд
    :return: UUID сессии
    """
    user_data[names.ID_USER] = id_user
    sql = "INSERT INTO Users" \
          " VALUES ({id_user},\'{Name}\','',\'{Email}\'," \
          "\'{Sex}\',\'{City}\',\'{Educational}\',\'{Logo}\'" \
          ")".format(**user_data)
    gs.SqlQuery(sql)
    return input_session_table(id_user, connect, current_connect)


def input_session_table(id_user, connect=None, current_connect=None):
    """
    Конечный метод, регистрирует данные в таблицы "Сессии пользователей"
    :param id_user: int ID пользователя
    :param connect: соединение с бд
    :param current_connect: соединение с бд
    :return: UUID сессии
    """
    UUID = uuid.uuid4()
    sql = "INSERT INTO Session (id_user, uuid)" \
          " VALUES ({id}, \'{UUID}\')".format(id=id_user, UUID=UUID)
    gs.SqlQuery(sql)
    return {names.ANSWER: names.SUCCESS, names.DATA: {"UUID": str(UUID)}}
