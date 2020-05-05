# coding: utf8
import hashlib
from api.service import GameService as gs
import api.base_name as names


def user_cabinet(data):
    """
    Функция подключается к базе данных,находит пользователя по id, который был получен на вход.
    Проверяет, что id не пустой. Возвращает json с данными о пользователе.
    """
    if data[names.ID_USER] is None:
        data[names.ID_USER] = "Empty"
        return {names.ANSWER: names.ERROR, names.DATA: data}
    if gs.check_id(data[names.ID_USER]) == False:
        return {names.ANSWER: "Id not found", names.DATA: data}
    sql = "SELECT Name, City, Sex, Email, Logo, Educational FROM users " \
          "where id_user = '{}'".format(data[names.ID_USER])
    print(sql)
    result = gs.SqlQuery(sql)

    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def change_password(data):
    """
    Функция получает json с id пользователя, старым паролем и новым.
    Проверяет элементы data, None или нет.
    Покдлючается к базе данных с помощью функции db_connect(), получает хеш пароля в базе по id.
    Если хеш от old_password==паролю в базе, то записывает в базу хеш new_password.
    Если все успешно, то функция вернет {names.ANSWER: 'Succes'}, если не верный пароль - {names.ANSWER: 'Wrong password'}
    """
    for i in data:
        if data[i] is None:
            data[i] = "Empty"
            return {names.ANSWER: names.ERROR, names.DATA: data}
    if gs.check_id(data[names.ID_USER]) == False:
        return {names.ANSWER: "Id not found", names.DATA: data}
    else:
        sql = "SELECT password FROM auth where id_user = '{}'".format(data[names.ID_USER])
        result = gs.SqlQuery(sql)
        password_hash = hashlib.md5()
        password_hash.update(data['Old_password'].encode())
        data['Old_password'] = password_hash.hexdigest()
        if data['Old_password'] == result[0]["password"]:
            password_hash = hashlib.md5()
            password_hash.update(data['New_password'].encode())
            data['New_password'] = password_hash.hexdigest()
            sql = "UPDATE auth SET password='{}' WHERE id_user='{}'".format(data["New_password"], data[names.ID_USER])
            gs.SqlQuery(sql)
            return {names.ANSWER: names.SUCCESS}
        else:
            return {names.ANSWER: "Wrong password"}


def edit_cabinet(data):
    """
     Функция получает json с id пользователя, и информацией о пользователе.
     Проверяет элементы data, None или нет.
     Покдлючается к базе данных с помощью функции db_connect().
     Проверка есть ли id в с помощью функции check_id
     Получает информацию о пользователе и перезаписывает поля в базе на те, что функция получила на вход
     Если все успешно, то функция вернет {names.ANSWER: 'Succes'} и data.
    """
    for i in data:
        if data[i] is None:
            data[i] = "Empty"
            return {names.ANSWER: names.ERROR,
                    names.DATA: data}
    if gs.check_id(data[names.ID_USER]) == False:
        return {names.ANSWER: "Id not found",
                names.DATA: data}
    else:
        sql = "UPDATE users SET Name='{}', Email='{}', Sex='{}', City='{}'," \
              " Educational='{}', Logo='{}', surname = '{}' WHERE id_user='{}'".format(
            data[names.NAME], data[names.EMAIL], data[names.SEX], data[names.CITY],
            data[names.EDUCATION], data[names.LOGO], data['Surname'], data[names.ID_USER]
            )
        gs.SqlQuery(sql)
        return {names.ANSWER: names.SUCCESS, names.DATA: data}