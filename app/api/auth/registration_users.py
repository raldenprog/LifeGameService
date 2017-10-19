# coding=utf-8
import hashlib
import logging
import uuid
from api.database.connect_db import db_connect
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def registration_user(user_data):
    check = ['Login', 'Password', 'Name',
             'Surname', 'Email', 'Sex',
             'City', 'Educational', 'Logo_name', 'Logo']
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
        return {"Answer": "Error", 'Data': registration_data}
    # TODO: Загрузить логотип в файл
    """
    with open('../app/resources/logo_users/{}'.format(user_data.get('Logo_name')), 'wb') as logo_file:
        logo_file.write(user_data['Logo'])
        registration_data['Logo'] = 'True'
    """
    answer = input_auth_table(registration_data)
    if answer.get('Answer') is not "Success":
        return {'Answer': 'Warning', "Data": "Ошибка запроса к базе данных"}
    return answer


def input_auth_table(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Warning", "Data": "Ошибка доступа к базе данных, повторить позже"}
    password_hash = hashlib.md5()
    password_hash.update(user_data['Password'].encode())
    user_data['Password'] = password_hash.hexdigest()
    sql = "INSERT INTO Auth" \
        " VALUES (null,\"{Login}\",\"{Password}\")".format(
            Login=user_data.get('Login'),
            Password=user_data.get('Password'))
    print(sql)
    try:
        current_connect.execute(sql)
        connect.commit()
        current_connect.execute("select last_insert_id()")
        id_user = current_connect.fetchone()
    except:
        logging.error('error: Ошибка запроса к базе данных')
        return {'Answer': 'Warning', "Data": "Ошибка запроса к базе данных"}
    return input_access_table(id_user.get('last_insert_id()'), user_data, connect, current_connect)


def input_access_table(id_user, user_data, connect, current_connect):
    sql = "INSERT INTO Access" \
        " VALUES ({id},0)".format(id=id_user)
    print(sql)
    try:
        current_connect.execute(sql)
        connect.commit()
    except:
        logging.error('error: Ошибка запроса к базе данных')
        return {'Answer': 'Warning', "Data": "Ошибка запроса к базе данных"}
    return input_user_table(id_user, user_data, connect, current_connect)


def input_user_table(id_user, user_data, connect, current_connect):

    sql = "INSERT INTO Users" \
        " VALUES ({id_user},\"{Name}\",\"{Surname}\",\"{Email}\"," \
        "\"{Sex}\",\"{City}\",\"{Educational}\",\"{Logo}\"" \
        ")".format(**user_data, id_user=id_user)
    print(sql)
    try:
        current_connect.execute(sql)
        connect.commit()
    except:
        logging.error('error: Ошибка запроса к базе данных')
        return {'Answer': 'Warning', "Data": "Ошибка запроса к базе данных"}
    return input_session_table(id_user, connect, current_connect)


def input_session_table(id_user, connect, current_connect):
    UUID = uuid.uuid4()
    sql = "INSERT INTO Session" \
        " VALUES (null, {id}, \"{UUID}\")".format(id=id_user, UUID=UUID)
    print(sql)
    try:
        current_connect.execute(sql)
        connect.commit()
        connect.close()
    except:
        logging.error('error: Ошибка запроса к базе данных')
        return {'Answer': 'Warning', "Data": "Ошибка запроса к базе данных"}
    print(UUID)
    return {'Answer': 'Success', 'Data': {"UUID": str(UUID)}}
