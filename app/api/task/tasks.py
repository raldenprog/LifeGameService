# -*- coding: utf-8 -*-
import pymysql
import logging
from api.database.connect_db import db_connect

logging.basicConfig(filename='logger.log',
                    format='%(asctime)s %(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s',
                    level=logging.INFO)

def empty_task_data():
    return {
            "task_category" :   "Unchecked",
            "task_name" :       "Unchecked",
            "task_flag" :       "Unchecked",
            "task_description" :"Unchecked",
            "task_point" :      "Unchecked",
            "task_hint" :       "Unchecked",
            #"task_solve" :      "Unchecked",
            "task_link" :       "Unchecked"
            #"status"    :       "Unchecked",
            #"puplic_status" :   "Unchecked",
            #"event"         :   "Unchecked",
            #"database" :        "Unchecked"
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
    check_field = ["task_category", "task_name", "task_flag", "task_description",
                   "task_point", "task_hint", "task_link"]#, "task_solve", "status",
                   #"public_status", "event"]

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
        #check_data["database"] = "Connected"
    except:
        #check_data["database"] = "Disconnected"
        logging.error('Fatal error: param \'database\' disconnected')
        return {"answer": "Error",
                "data": check_data}
    else:
        try:
            sql = "INSERT INTO task" \
                " VALUES (null,\"{task_category}\",\"{task_name}\"," \
                "\"{task_flag}\",\"{task_description}\",{task_point},\"{task_hint}\"," \
                "null, \"{task_link}\",1,1,1)".format(**data)
            print(sql)
            current_connect.execute(sql)
            connect.commit()
            #check_data["database"] = "Recorded"
        except Exception as e:
            if e == 1062:
                return {"Answer": "Warning",
                        "Data": 'Duplicate task'}
            logging.error('Fatal error: param \'sql\' can\'t create new record')
            #check_data["database"] = "Unrecorded"
            return {"Answer": "Warning",
                    "Data": check_data}
        finally:
            connect.close()
    if error_flag:
        return {"Answer": "Error",
                "Data": check_data}
    else:
        return {"Answer": "Success"}

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
        print ("Except 1")
        logging.error('Fatal error in function \'create_few_tasks\', param \'batch_data\'')
        return {"answer": "Error",
                "data": None,
                "number": 0}

    try:
        for data in batch_data:
            answer = create_one_task(data)
            answers.append(answer)
    except:
        print ("Except 2")
        logging.error('Fatal error in function \'create_few_tasks\', param \'data\'')
        return {"answer": "Error",
                "data": None,
                "number": 0}

    return {"answer": "Success",
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


def get_task_event_name(event, task_name):
    connect, current_connect = db_connect()
    sql = "SELECT ID_Task, Task_name, Task_category, Task_description FROM task WHERE event={} AND ID_Task={}".format(event, task_name)

    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}


def get_task_event_category(event, task_category):
    connect, current_connect = db_connect()
    sql = "SELECT ID, task_name, task_category, event FROM task WHERE event={} AND task_category={}".format(event, task_category)

    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error'}
    return {'Answer': 'Success', 'data': result}


def get_task_acc(id_task, id_user):
    connect, current_connect = db_connect()
    sql = "SELECT 1 FROM task_acc WHERE id_task = {} and id_user = {}".format(id_task, id_user)
    print(sql)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchone()
    except:
        logging.error('Fatal error: execute database')
        return False
    try:
        if len(result) == 1:
            return True
    except:
        return False


def preparation_result(data, id_user):
    result = []
    print(data)
    for item in data:
        temp = dict()
        for id, value in item.items():
            if id == 'ID_Task':
                temp['Close'] = get_task_acc(value, id_user)
            else:
                if isinstance(value, str):
                    temp[id] = value.encode('UTF-8').decode('UTF-8')
                else:
                    temp[id] = value
            #print(id, value)
        result.append(temp)
    return result


def get_task_event(data):
    connect, current_connect = db_connect()
    sql = "SELECT ID_Task, Task_name, Task_category, Task_point, " \
          "Task_description, Task_hint, Task_link FROM task WHERE id_event={}".format(data['id_event'])
    print(sql)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchall()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error connect db'}
    return {'Answer': 'Success', 'Data': preparation_result(result, data['id_user'])}


def input_task_acc(user_data):
    connect, current_connect = db_connect()
    if connect == -1:
        return {"Answer": "Warning", "Data": "Ошибка доступа к базе данных, повторить позже"}

    sql = "INSERT INTO task_acc" \
        " VALUES (null,{},{},{})".format(user_data['ID_Task'], user_data['id_user'], user_data['Task_point'])
    print(sql)
    try:
        current_connect.execute(sql)
        connect.commit()
    except:
        logging.error('error: Ошибка запроса к базе данных. Возможно такой пользователь уже есть')
        return {'Answer': 'Warning', "Data": "Ошибка запроса к базе данных."}
    return True


def check_task(data):
    connect, current_connect = db_connect()
    sql = "SELECT ID_Task, Task_point FROM task WHERE Task_name = '{}' and Task_flag = '{}'".format(
        data['Task_name'],
        data['Task_flag'])
    print(sql)
    try:
        current_connect.execute(sql)
        result = current_connect.fetchone()
    except:
        logging.error('Fatal error: execute database')
        return {'Answer': 'Error connect db'}
    try:
        if len(result) == 2:
            result['id_user'] = data['id_user']
            input_task_acc(result)
            return {'Answer': 'Success', 'Data': True}
    except:
        return {'Answer': 'Warning', 'Data': False}

#print (create_few_tasks(json))