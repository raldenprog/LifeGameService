import logging
import hashlib

#for other OS
from app.api.database.connect_db import db_connect

#for Linux
'''
import sys
import os
directory_user_cabinet= os.getcwd()
directory_user_cabinet=directory_user_cabinet.split("user_cabinet")[0]
directory_user_cabinet+="database"
sys.path.insert(0, directory_user_cabinet)
from connect_db import db_connect
'''



logging.basicConfig(filename='logger.log',
                    format='%(asctime)s %(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s',
                    level=logging.INFO)


def user_cabinet(data):
    """
    Входные данные:
    json{"id": "Value"
        }
        
    Выходные данные:
    json{"id": "Value",
        "login": "Value",
        "password": "anton",
        "name": "Value",
        "patronymic": "Value",
        "email": "Value",
        "sex": "Value",
        "city": "Value",
        "Educational": "Value",
        "logo": "Value",
        "is_admin": "Value",
        "is_captain": "Value",
        "is_moderator": "Value",
        }
        
        Функция подключается к базе данных,находит пользователя по id, который был получен на вход.
        Проверяет, что id не пустой. Возвращает json с данными о пользователе.
    """
    try:
        if data["id"] is None:
            logging.info('Incorrect parameter id - None')
            data["id"] = "Empty"
            return {"Answer": "Error",
                    "data": data}
    except:
        logging.error('Fatal error: param id')
        return {"Answer": "Error",
                "data": data}
    try:
        current_connect = db_connect().cursor()
    except:
        logging.error('Fatal error: connect database')
        return {"Answer": "Error",
                "data": data}
    else:
        try:
            current_connect.execute("SELECT * FROM users where id = '{}'".format(
                data['id']
            ))
            db_connect().commit()
            result = current_connect.fetchall()
            return {"Answer": "Success",
                    "data": result}
        except:
            logging.error('Fatal error: execute database')
            return {"Answer": "Error"}


def change_password(data):
    """
    Входные данные:
     data = {"id": "1",
        "old_password": "pinlox123",
        "new_password": "qwerty"
        }

    Выходные данные:
    {"Answer": "Succes"}

    Функция получает json с id пользователя, старым паролем и новым.
    Проверяет элементы data, None или нет.
    Покдлючается к базе данных с помощью функции db_connect(), получает хеш пароля в базе по id.
    Если хеш от old_password==паролю в базе, то записывает в базу хеш new_password.
    Если все успешно, то функция вернет {'Answer': 'Succes'}, если не верный пароль - {'Answer': 'Wrong password'}

    """
    try:
        for i in data:
            if data[i] is None:
                logging.info('Incorrect parameter '+i+' - None')
                data[i] = "Empty"
                return {"Answer": "Error",
                        "data": data}
    except:
        logging.error('Fatal error: check data is None')
        return {"Answer": "Error",
                "data": data}
    try:
        connect = db_connect()
        current_connect = connect.cursor()
    except:
        logging.error('Fatal error: connect database')
        return {"Answer": "Error",
            "data": data}
    else:
        try:
            current_connect.execute("SELECT password FROM users where id = '{}'".format(
                data['id']
            ))
            result = current_connect.fetchall()
        except:
            logging.error('Fatal error: execute database')
            return {"Answer": "Error"}
        else:
            try:
                password_hash = hashlib.md5()
                password_hash.update(data['old_password'].encode())
                data['old_password'] = password_hash.hexdigest()
                if data['old_password'] == result[0]['password']:
                    password_hash = hashlib.md5()
                    password_hash.update(data['new_password'].encode())
                    data['new_password'] = password_hash.hexdigest()
                    sql = "UPDATE users SET password='{}' WHERE id='{}'".format(
                        data["new_password"], data["id"]
                    )
                    current_connect.execute(sql)
                    connect.commit()
                    connect.close()
                    return {"Answer": "Succes"}
                else:
                    return {"Answer": "Wrong password"}
            except:
                logging.error('Fatal error: Password comparison')
                return {"Answer": "Error"}


def edit_cabinet(data):
    """
        Входные данные:
         json{"id": "Value",
            "name": "Value",
            "patronymic": "Value",
            "email": "Value",
            "sex": "Value",
            "city": "Value",
            "Educational": "Value",
            "logo": "Value",
            }

        Выходные данные:
        {"Answer": "Succes"}
        json{"id": "Value",
            "login": "Value",
            "password": "anton",
            "name": "Value",
            "patronymic": "Value",
            "email": "Value",
            "sex": "Value",
            "city": "Value",
            "Educational": "Value",
            "logo": "Value",
            "is_admin": "Value",
            "is_captain": "Value",
            "is_moderator": "Value",
            }

             Функция получает json с id пользователя, и информацией о пользователе.
             Проверяет элементы data, None или нет.
             Покдлючается к базе данных с помощью функции db_connect(),
             Получает количество id в базе и если data["id"]<= количеству, то данный id есть.
             Получает информацию о пользователе и перезаписывает поля в базе на те, что функция получила на вход
             Если все успешно, то функция вернет {'Answer': 'Succes'} и data.
        """
    try:
        for i in data:
            if data[i] is None:
                logging.info('Incorrect parameter '+i+' - None')
                data[i] = "Empty"
                return {"Answer": "Error",
                        "data": data}
    except:
        logging.error('Fatal error: check data is None')
        return {"Answer": "Error",
                "data": data}
    try:
        connect = db_connect()
        current_connect = connect.cursor()
    except:
        logging.error('Fatal error: connect database')
        return {"Answer": "Error",
                "data": data}
    else:
        try:
            check_id=0
            sql = "SELECT id FROM users"
            current_connect.execute(sql)
            result = current_connect.fetchall()
            if len(result) >= int(data["id"]):
                check_id=1
            if check_id==0:
                return {"Answer": "Id not found",
                        "data": data}
        except:
            logging.error('Fatal error: check id')
            return {"Answer": "Error",
                    "data": data}
        else:
            try:
                sql = "UPDATE users SET name='{}', patronymic='{}', email='{}', sex='{}', city='{}', Educational='{}', logo='{}' WHERE id='{}'".format(
                    data["name"], data["patronymic"], data["email"], data["sex"], data["city"], data["Educational"], data["logo"], data["id"]
                    )
                current_connect.execute(sql)
                connect.commit()
                connect.close()
                return {"Answer": "Succes",
                        "data": data
                        }
            except:
                logging.error('Fatal error: Password comparison')
                return {"Answer": "Error"}