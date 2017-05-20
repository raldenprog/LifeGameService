import pymysql
import hashlib
import logging


logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def login_verification(user_data):
    check = ['login', 'password']
    registration_data = {
        'login': '', 'password': ''
    }
    for data in check:
        try:
            if user_data[data] is None:
                logging.info('Incorrect parameter ' + data)
                return {"Answer": "Error"}
            else:
                registration_data[data] = user_data[data]
        except:
            logging.error('Fatal error in function fun, param ' + data)
            return {"Answer": "Error"}
    return get_user(registration_data)


def get_user(user_data):
    try:
        connect = pymysql.connect(host='5.137.232.44',
                                  user='dev_life_user',
                                  password='pinlox123',
                                  db='life_game_service_database',
                                  cursorclass=pymysql.cursors.DictCursor)
        current_connect = connect.cursor()
    except:
        logging.error('Fatal error in function input_user_table, connect database')
        return {"Answer": "Error"}
    else:
        try:
            password_hash = hashlib.md5()
            password_hash.update(user_data['password'].encode())
            user_data['password'] = password_hash.hexdigest()
            current_connect.execute("SELECT * FROM users where login = '{}' and password = '{}'".format(
                user_data['login'], user_data['password']
            ))
            connect.commit()
        except:
            logging.error('Fatal error in function input_user_table, execute database')
            return {"Answer": "Error"}
        result = current_connect.fetchall()
        connect.close()
        if len(result) != 0:
            return {"Answer": "Success"}
        return {"Answer": "Error"}
