# coding: utf8
import logging
import hashlib
from api.database.connect_db import db_connect
from api.user_cabinet.id_check import check_id

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


def user_cabinet(data):
    """
    Функция подключается к базе данных,находит пользователя по id, который был получен на вход.
    Проверяет, что id не пустой. Возвращает json с данными о пользователе.
    """
    try:
        if data["id_user"] is None:
            logging.info('Incorrect parameter id_user - None')
            data["id_user"] = "Empty"
            return {"Answer": "Error", "Data": data}
    except:
        logging.error('Fatal error: param id_user')
        return {"Answer": "Error", "Data": data}
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Error"}
    try:
        if check_id(data["id_user"], current_connect) == 0:
            return {"Answer": "id_user not found", "Data": data}
    except:
        logging.error('Fatal error: check id_user')
        return {"Answer": "Error", "Data": data}
    try:
        current_connect.execute("SELECT * FROM Users where user = '{}'".format(
            data['id_user']
        ))
        connect.commit()
        result = current_connect.fetchall()[0]
        connect.close()
        return {"Answer": "Success", "Data": result}
    except:
        logging.error('Fatal error: execute database')
        return {"Answer": "Error"}


def change_password(data):
    """
    Функция получает json с id пользователя, старым паролем и новым.
    Проверяет элементы data, None или нет.
    Покдлючается к базе данных с помощью функции db_connect(), получает хеш пароля в базе по id.
    Если хеш от old_password==паролю в базе, то записывает в базу хеш new_password.
    Если все успешно, то функция вернет {'Answer': 'Succes'}, если не верный пароль - {'Answer': 'Wrong password'}
    """
    try:
        for i in data:
            if data[i] is None:
                logging.info('Incorrect parameter ' + i + ' - None')
                data[i] = "Empty"
                return {"Answer": "Error", "Data": data}
    except:
        logging.error('Fatal error: check data is None')
        return {"Answer": "Error", "Data": data}
    try:
        connect, current_connect = db_connect()
    except:
        logging.error('Fatal error: connect database')
        return {"Answer": "Error", "Data": data}
    try:
        if (check_id(data["id"], current_connect)) == 0:
            return {"Answer": "Id not found", "Data": data}
    except:
        logging.error('Fatal error: check id')
        return {"Answer": "Error", "Data": data}
    else:
        try:
            current_connect.execute("SELECT Password FROM Users where ID = '{}'".format(data['ID']))
            result = current_connect.fetchall()[0]
        except:
            logging.error('Fatal error: execute database')
            return {"Answer": "Error"}
        else:
            try:
                password_hash = hashlib.md5()
                password_hash.update(data['Old_password'].encode())
                data['Old_password'] = password_hash.hexdigest()
                if data['Old_password'] == result['Password']:
                    password_hash = hashlib.md5()
                    password_hash.update(data['New_password'].encode())
                    data['New_password'] = password_hash.hexdigest()
                    sql = "UPDATE Users SET Password='{}' WHERE ID='{}'".format(data["New_password"], data["ID"])
                    current_connect.execute(sql)
                    connect.commit()
                    connect.close()
                    return {"Answer": "Success"}
                else:
                    return {"Answer": "Wrong password"}
            except:
                logging.error('Fatal error: Password comparison')
                return {"Answer": "Error"}

def edit_cabinet(data):
    """
             Функция получает json с id пользователя, и информацией о пользователе.
             Проверяет элементы data, None или нет.
             Покдлючается к базе данных с помощью функции db_connect().
             Проверка есть ли id в с помощью функции check_id
             Получает информацию о пользователе и перезаписывает поля в базе на те, что функция получила на вход
             Если все успешно, то функция вернет {'Answer': 'Succes'} и data.
        """
    try:
        for i in data:
            if data[i] is None:
                logging.info('Incorrect parameter '+i+' - None')
                data[i] = "Empty"
                return {"Answer": "Error",
                        "Data": data}
    except:
        logging.error('Fatal error: check data is None')
        return {"Answer": "Error",
                "Data": data}
    try:
        connect, current_connect = db_connect()
    except:
        logging.error('Fatal error: connect database')
        return {"Answer": "Error",
                "Data": data}
    else:
        try:
            data = data['data']
            sql = "UPDATE Users SET Name='{}', Surname='{}', Email='{}', Sex='{}', City='{}'," \
                    " Educational='{}', Logo='{}' WHERE user='{}'".format(
                data["Name"], data["Surname"], data["Email"], data["Sex"], data["City"],
                data["Educational"], data["Logo"], data["id_user"]
                )
            current_connect.execute(sql)
            connect.commit()
            connect.close()
            return {"Answer": "Success", "Data": data}
        except:
            logging.error('Fatal error: Password comparison')
            return {"Answer": "Error"}

