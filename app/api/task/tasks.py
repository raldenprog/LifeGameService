# coding: utf-8
import pymysql
import logging
from app.api.database.connect_db import db_connect

logging.basicConfig(filename='logger.log',
                    format='%(asctime)s %(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s',
                    level=logging.INFO)

def empty_task_data():
    return { "id" :             "Unchecked",
            "task_category" :   "Unchecked",
            "task_name" :       "Unchecked",
            "task_flag" :       "Unchecked",
            "task_description" :"Unchecked",
            "task_point" :      "Unchecked",
            "task_hint" :       "Unchecked",
            "task_solve" :      "Unchecked",
            "task_link" :       "Unchecked",
            "status"    :       "Unchecked",
            "puplic_status" :   "Unchecked",
            "event"         :   "Unchecked",
            "database" :        "Unchecked"
            }

'''
Данная функция отвечает за обработку отдельного блока формата JSON
для загрузки тасков в систему. Функиция возвращает
статус завершения вцелом и статусы обработки каждого элемента.
Таким образом, можно определить проблемнный элемент. Также, в лог
выведется причина возникновения проблемы.

P.S. Обратите внимание, что в списке статусов элементов присутствует
поле 'database' - которое описывает состояние базы данных на момент
возникновения проблемы:

Connected - к базе данных есть доступ,
Disconnected - нет доступа к базе данных,
Recorded - таск успешно записан в базу,
Unrecorded - таск не залит в базу
'''

def create_one_task(data):
    check_field = ["id", "task_category", "task_name", "task_flag", "task_description",
                   "task_point", "task_hint", "task_solve", "task_link", "status",
                   "public_status", "event"]

    error_flag = 0
    check_data = empty_task_data()
    for check in check_field:
        try:
            if data[check] is None:
                error_flag = 1
                logging.info('Incorrect parameter \'%s\' - None' % check)
                check_data[check] = "Error"
            else:
                check_data[check] = "Success"
        except:
            error_flag = 1
            logging.error('Fatal error param \'%s\'' % check)

    if error_flag:
        return {"answer": "Error",
                "data": check_data}
    try:
        connect, current_connect = db_connect()
        check_data["database"] = "Connected"
    except:
        check_data["database"] = "Disconnected"
        logging.error('Fatal error: param \'database\' disconnected')
        return {"answer": "Error",
                "data": check_data}
    else:
        try:
            sql = "INSERT INTO task" \
                " VALUES (null,\"{id}\",\"{task_category}\",\"{task_name}\"," \
                "\"{task_flag}\",\"{task_description}\",\"{task_point}\",\"{task_hint}\"," \
                "\"{task_solve}\",\"{task_link}\",\"{status}\",\"{public_status}\",\"{event}\")".format(**data)
            print(sql)
            current_connect.execute(sql)
            connect.commit()
            connect.close()
            check_data["database"] = "Recorded"
        except:
            logging.error('Fatal error: param \'sql\' can\'t create new record')
            check_data["database"] = "Unrecorded"
            return {"answer": "Error",
                    "data": check_data}
    if error_flag:
        return {"answer": "Error",
                "data": check_data}
    else:
        return {"answer": "Success",
                "data": check_data}

'''
Данная функция принимает на вход массив из JSON записей
формата {"data_1" : "value_1"},{"data_2" : "value_2"},{"data_3" : "value_3"}.

НЕ {{"data_1" : "value_1"},{"data_2" : "value_2"},{"data_3" : "value_3"}} ПОЖАЛУЙСТА.

Так же, на вход принемается и один элемент. В случае успеха
функция возвращает статус завершения, список всех элементов
внутри массива JSON с их статусами и количество элементов в целом.

В случае неудачи - функция возвращает статус завершения,
проблемный элемент массива, и номер элемента, начиная с ЕДИНИЦЫ (1, one)
Так как внутри функции вызывается create_one_task, то основное логирование
происходит внутри неё.
'''

def create_few_tasks(batch_data):
    answers = []
    try:
        if len(batch_data) <= 0:
            print (len(batch_data))
            return {"answer": "Error",
                    "data": None,
                    "number": 0}
    except:
        print "Except 1"
        logging.error('Fatal error in function \'create_few_tasks\', param \'batch_data\'')
        return {"answer": "Error",
                "data": None,
                "number": 0}

    try:
        for data in batch_data:
            answer = create_one_task(data)
            answers.append(answer)
    except:
        print "Except 2"
        logging.error('Fatal error in function \'create_few_tasks\', param \'data\'')
        return {"answer": "Error",
                "data": None,
                "number": 0}

    return {"answer": "Ok",
            "data": answers,
            "number": len(batch_data)}

json = {    "id" :              "1",
            "task_category" :   2,
            "task_name" :       3,
            "task_flag" :       4,
            "task_description" :5,
            "task_point" :      6,
            "task_hint" :       7,
            "task_solve" :      8,
            "task_link" :       9
        },\
       {    "id" :              "11",
            "task_category" :   21,
            "task_name" :       31,
            "task_flag" :       41,
            "task_description" :51,
            "task_point" :      62,
            "task_hint" :       73,
            "task_solve" :      84,
            "task_link" :       95
            }

def get_task_event_name(data):
    connect, current_connect = db_connect()
    sql = "SELECT event, name FROM task".format(data)

    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}

def get_task_event_category(data):
    connect, current_connect = db_connect()
    sql = "SELECT event, task_category FROM task".format(data)

    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}

def get_task_event(data):
    connect, current_connect = db_connect()

    sql = "SELECT event FROM task".format(data)

    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}


print create_few_tasks(json)