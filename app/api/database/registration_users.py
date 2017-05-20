import pymysql
import hashlib
import logging

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def add_user(user_data):
    check = ['login', 'password', 'name',
             'patronymic', 'email', 'sex',
             'city', 'Educational', 'logo_name', 'logo']
    registration_data = {
        'login': '', 'password': '', 'name': '',
        'patronymic': '', 'email': '', 'sex': '',
        'city': '', 'Educational': '', 'logo_name': '', 'logo': ''
    }
    flag = False
    for data in check:
        try:
            if user_data[data] is None:
                logging.info('Incorrect parameter ' + data)
                registration_data[data] = 'Error'
                flag = True
            else:
                registration_data[data] = user_data[data]
        except:
            logging.error('Fatal error: param ' + data)
            registration_data[data] = 'Error'
            flag = True
    if flag:
        return {"Answer": "Error", 'Data': registration_data}
    with open('../app/resources/logo_users/{}'.format(user_data['logo_name']), 'w') as logo_file:
        logo_file.write(user_data['logo'])
        registration_data['logo'] = 'True'
    return input_user_table(registration_data)


def input_user_table(user_data):
    try:
        connect = pymysql.connect(host='5.137.227.36',
                                  user='dev_life_user',
                                  password='pinlox123',
                                  db='life_game_service_database',
                                  cursorclass=pymysql.cursors.DictCursor)
        current_connect = connect.cursor()
    except:
        logging.error('Fatal error: connect database')
        return {'Answer': 'Error'}
    else:
        password_hash = hashlib.md5()
        password_hash.update(user_data['password'].encode())
        user_data['password'] = password_hash.hexdigest()
        try:
            sql = "INSERT INTO users" \
                " VALUES (null,\"{login}\",\"{password}\",\"{name}\"," \
                "\"{patronymic}\",\"{email}\",\"{sex}\",\"{city}\"," \
                "\"{Educational}\",\"{logo}\", 1, 1, 1)".format(**user_data)
            print(sql)
            current_connect.execute(sql)
            connect.commit()
            connect.close()
        except:
            logging.error('Fatal error: execute database')
            return {'Answer': 'Error'}

        return {'Answer': 'Success'}
