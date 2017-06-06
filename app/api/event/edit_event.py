import logging
from app.api.database.connect_db import db_connect


logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def registration_event(user_data):
    check = ['name', 'description', 'logo',
             'status', 'date_start', 'date_end',
             'date_stop', 'date_continue']
    registration_data = {
        'name': '', 'description': '', 'logo': '',
        'status': '', 'date_start': '', 'date_end': '',
        'date_stop': '', 'date_continue': ''
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
    return input_event_table(registration_data)


def input_event_table(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Error"}
    try:
        sql = "INSERT INTO event" \
            " VALUES (null,\"{name}\",\"{description}\",\"{logo}\"," \
            "\"{status}\",{date_start},{date_end},{date_stop}," \
            "{date_continue})".format(**user_data)
        print(sql)
        current_connect.execute(sql)
        connect.commit()
        connect.close()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}

    return {'Answer': 'Success'}


def update_event(user_data):
    check = ['id', 'name', 'description', 'logo',
             'status', 'date_start', 'date_end',
             'date_stop', 'date_continue']
    update_data = {
        'id': '', 'name': '', 'description': '', 'logo': '',
        'status': '', 'date_start': '', 'date_end': '',
        'date_stop': '', 'date_continue': ''
    }
    flag = False
    for data in check:
        try:
            if user_data[data] is None:
                logging.info('Incorrect parameter ' + data)
                update_data[data] = 'Error'
                flag = True
            else:
                update_data[data] = user_data[data]
        except:
            logging.error('Fatal error: param ' + data)
            update_data[data] = 'Error'
            flag = True
    if flag:
        return {"Answer": "Error", 'Data': update_data}
    return update_event_table(update_data)


def update_event_table(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Error"}
    try:
        sql = "UPDATE event SET" \
            "name='{name}', description='{description}', logo='{logo}', status='{status}', date_start='{date_start}'," \
            " date_end='{date_end}', date_stop='{date_stop}', date_continue='{date_continue}' WHERE id='{id}'".format(**user_data)
        print(sql)
        current_connect.execute(sql)
        connect.commit()
        connect.close()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}

    return {'Answer': 'Success'}


def delete_event(user_data):
    pass
