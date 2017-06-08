import hashlib
import logging
from app.api.database.connect_db import db_connect
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def add_user(user_data):
    check = ['Login', 'Password', 'Name',
             'Patronymic', 'Email', 'Sex',
             'City', 'Educational', 'Logo_name', 'Logo']
    registration_data = {'Login': '', 'Password': '', 'Name': '',
        'Patronymic': '', 'Email': '', 'Sex': '',
        'City': '', 'Educational': '', 'Logo_name': '', 'Logo': ''}
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
    with open('../app/resources/logo_users/{}'.format(user_data['Logo_name']), 'w') as logo_file:
        logo_file.write(user_data['Logo'])
        registration_data['Logo'] = 'True'
    return input_user_table(registration_data)


def input_user_table(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Error"}
    password_hash = hashlib.md5()
    password_hash.update(user_data['Password'].encode())
    user_data['Password'] = password_hash.hexdigest()
    try:
        sql = "INSERT INTO users" \
            " VALUES (null,\"{Login}\",\"{Password}\",\"{Name}\"," \
            "\"{Patronymic}\",\"{Email}\",\"{Sex}\",\"{City}\"," \
            "\"{Educational}\",\"{Logo}\", 1, 1, 1)".format(**user_data)
        print(sql)
        current_connect.execute(sql)
        connect.commit()
        connect.close()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}

    return {'Answer': 'Success'}
