# coding: utf8
import logging
import hashlib
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


def user_cabinet(data):
    """
    Функция подключается к базе данных,находит пользователя по id, который был получен на вход.
    Проверяет, что id не пустой. Возвращает json с данными о пользователе.
    """
    try:
        if data[names.ID_USER] is None:
            logging.info('Incorrect parameter id - None')
            data[names.ID_USER] = "Empty"
            return {names.ANSWER: names.ERROR, names.DATA: data}
    except:
        logging.error('Fatal error: param id')
        return {names.ANSWER: names.ERROR, names.DATA: data}
    try:
        if data[names.ID_USER].isdigit() == False:
            return {names.ANSWER: names.ERROR, names.DATA: data}
    except:
        logging.error('Fatal error: type id')
        return {names.ANSWER: names.ERROR, names.DATA: data}
    try:
        if gs.check_id(data[names.ID_USER]) == False:
            return {names.ANSWER: "Id not found", names.DATA: data}
    except:
        logging.error('Fatal error: check id')
        return {names.ANSWER: names.ERROR, names.DATA: data}
    try:
        sql = "SELECT Name, City, Sex, Email, Logo, Educational FROM users " \
              "where id_user = '{}'".format(data[names.ID_USER])
        result = gs.SqlQuery(sql)
        return {names.ANSWER: names.SUCCESS, names.DATA: result}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}


def change_password(data):
    """
    Функция получает json с id пользователя, старым паролем и новым.
    Проверяет элементы data, None или нет.
    Покдлючается к базе данных с помощью функции db_connect(), получает хеш пароля в базе по id.
    Если хеш от old_password==паролю в базе, то записывает в базу хеш new_password.
    Если все успешно, то функция вернет {names.ANSWER: 'Succes'}, если не верный пароль - {names.ANSWER: 'Wrong password'}
    """
    try:
        for i in data:
            if data[i] is None:
                logging.info('Incorrect parameter ' + i + ' - None')
                data[i] = "Empty"
                return {names.ANSWER: names.ERROR, names.DATA: data}
    except:
        logging.error('Fatal error: check data is None')
        return {names.ANSWER: names.ERROR, names.DATA: data}
    try:
        if gs.check_id(data[names.ID_USER]) == False:
            return {names.ANSWER: "Id not found", names.DATA: data}
    except:
        logging.error('Fatal error: check id')
        return {names.ANSWER: names.ERROR, names.DATA: data}
    else:
        try:
            sql = "SELECT password FROM auth where id_user = '{}'".format(data[names.ID_USER])
            result = gs.SqlQuery(sql)
        except:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
        else:
            try:
                password_hash = hashlib.md5()
                password_hash.update(data['Old_password'].encode())
                data['Old_password'] = password_hash.hexdigest()
                if data['Old_password'] == result[0][names.PASSWORD]:
                    password_hash = hashlib.md5()
                    password_hash.update(data['New_password'].encode())
                    data['New_password'] = password_hash.hexdigest()
                    sql = "UPDATE auth SET password='{}' WHERE id_user='{}'".format(data["New_password"], data[names.ID_USER])
                    gs.SqlQuery(sql)
                    return {names.ANSWER: names.SUCCESS}
                else:
                    return {names.ANSWER: "Wrong password"}
            except:
                logging.error('Fatal error: Password comparison')
                return {names.ANSWER: names.ERROR}


def edit_cabinet(data):
    """
             Функция получает json с id пользователя, и информацией о пользователе.
             Проверяет элементы data, None или нет.
             Покдлючается к базе данных с помощью функции db_connect().
             Проверка есть ли id в с помощью функции check_id
             Получает информацию о пользователе и перезаписывает поля в базе на те, что функция получила на вход
             Если все успешно, то функция вернет {names.ANSWER: 'Succes'} и data.
        """
    try:
        for i in data:
            if data[i] is None:
                logging.info('Incorrect parameter '+i+' - None')
                data[i] = "Empty"
                return {names.ANSWER: names.ERROR,
                        names.DATA: data}
    except:
        logging.error('Fatal error: check data is None')
        return {names.ANSWER: names.ERROR,
                names.DATA: data}
    try:
        if gs.check_id(data[names.ID_USER]) == False:
            return {names.ANSWER: "Id not found",
                    names.DATA: data}
    except:
        logging.error('Fatal error: check id')
        return {names.ANSWER: names.ERROR,
                names.DATA: data}
    else:
        try:
            sql = "UPDATE users SET Name='{}', Email='{}', Sex='{}', City='{}'," \
                  " Educational='{}', Logo='{}', surname = '{}' WHERE id_user='{}'".format(
                data[names.NAME], data[names.EMAIL], data[names.SEX], data[names.CITY],
                data[names.EDUCATION], data[names.LOGO], data['Surname'], data[names.ID_USER]
                )
            print(sql)
            gs.SqlQuery(sql)
            return {names.ANSWER: names.SUCCESS, names.DATA: data}
        except:
            logging.error('Fatal error: Password comparison')
            return {names.ANSWER: names.ERROR}

data = {"Login": "test_user15",
        names.PASSWORD: "new_password",
        "Name": "new_name",
        "Surname": "test_Surname",
        "Email": "test_email@email.com",
        "Sex": "man",
        "City": "test_City",
        "Educational": "test_Educational",
        "Logo_name": "test_Logo_name",
        "Logo": "test_Logo",
        names.ID_USER: "15"
        }

print(edit_cabinet(data))