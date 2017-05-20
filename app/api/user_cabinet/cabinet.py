import pymysql
import logging

logging.basicConfig(filename='logger.log',
                    format='%(asctime)s %(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s',
                    level=logging.INFO)


def get_user():
    """
    тест функция возвращает json с id и login
    """
    return {"id": "1",
            "login": "Anton",
            }


print(get_user())


def user_cabinet(data):
    """
    получает json, проверка есть ли id, подключается к бд, возвращает инфу о пользователе
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
        connect = pymysql.connect(host='5.137.227.36',
                                  user='dev_life_user',
                                  password='pinlox123',
                                  db='life_game_service_database',
                                  cursorclass=pymysql.cursors.DictCursor)
        current_connect = connect.cursor()
    except:
        logging.error('Fatal error: connect database')
        return {"Answer": "Error",
                "data": data}
    else:
        try:
            current_connect.execute("SELECT * FROM users where id = '{}'".format(
                data['id']
            ))
            connect.commit()
            result = current_connect.fetchall()
            return {"Answer": "Ok",
                    "data": result}
        except:
            logging.error('Fatal error: execute database')
            return {"Answer": "Error"}


print(user_cabinet(get_user()))
