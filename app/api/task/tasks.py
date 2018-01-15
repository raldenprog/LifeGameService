# -*- coding: utf-8 -*-
import logging
from api.service import GameService as gs
import api.base_name as names
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
                check_data[check] = names.ERROR
            else:
                check_data[check] = "Success"
        except:
            error_flag = 1
            logging.error('Fatal error param \'%s\'' % check)

    if error_flag:
        return {names.ANSWER: names.ERROR,
                "data": check_data}
    try:
        sql = "INSERT INTO task" \
            " VALUES (null,\"{task_category}\",\"{task_name}\"," \
            "\"{task_flag}\",\"{task_description}\",{task_point},\"{task_hint}\"," \
            "null, \"{task_link}\",1,1,2)".format(**data)
        print(sql)
        gs.SqlQuery(sql)
        #check_data["database"] = "Recorded"
    except Exception as e:
        if e == 1062:
            return {names.ANSWER: names.WARNING,
                    "Data": 'Duplicate task'}
        logging.error('Fatal error: param \'sql\' can\'t create new record')
        #check_data["database"] = "Unrecorded"
        return {names.ANSWER: names.WARNING,
                "Data": check_data}
    if error_flag:
        return {names.ANSWER: names.ERROR,
                "Data": check_data}
    else:
        return {names.ANSWER: "Success"}

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
            return {names.ANSWER: names.ERROR,
                    "data": None,
                    "number": 0}
    except:
        print ("Except 1")
        logging.error('Fatal error in function \'create_few_tasks\', param \'batch_data\'')
        return {names.ANSWER: names.ERROR,
                "data": None,
                "number": 0}

    try:
        for data in batch_data:
            answer = create_one_task(data)
            answers.append(answer)
    except:
        print ("Except 2")
        logging.error('Fatal error in function \'create_few_tasks\', param \'data\'')
        return {names.ANSWER: names.ERROR,
                "data": None,
                "number": 0}

    return {names.ANSWER: "Success",
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
    sql = "SELECT ID_Task, Task_name, Task_category, Task_description FROM task WHERE event={} AND ID_Task={}".format(event, task_name)

    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: 'Success', 'data': result}


def get_task_event_category(event, task_category):
    sql = "SELECT id_task, task_name, task_category, event FROM task WHERE event={} AND task_category={}".format(event, task_category)

    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: 'Success', 'data': result}


def get_task_acc(id_task, id_user):
    sql = "SELECT id_task FROM task_acc WHERE id_task in {} and id_user = {}".format(id_task, id_user)
    print(sql)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {}
    try:
        print(result)
        if len(result) > 0:
            return result
    except:
        return {}


def preparation_result(data, id_user):
    result = []
    temp = dict()
    id_task = list()
    for item in data:
        item['Close'] = False
        id_task_temp = item.get('ID_Task')
        temp[id_task_temp] = item
        id_task.append(id_task_temp)
    #TODO: временное решение
    id_task = tuple(id_task)
    close_status = get_task_acc(id_task, id_user)
    if close_status is not None:
        for i in close_status:
            id_task = i['id_task']
            temp[id_task]['Close'] = True
    return data


def get_task_event(data):
    sql = "SELECT ID_Task, Task_name, Task_category, Task_point, " \
          "Task_description, Task_hint, Task_link FROM task WHERE id_event={} " \
          "order by Task_category, Task_point".format(data['id_event'])
    print(sql)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {names.ANSWER: 'Error connect db'}
    return {names.ANSWER: 'Success', 'Data': preparation_result(result, data['id_user'])}


def input_task_acc(user_data):
    #TODO: Временное решение.
    id_event = 2
    sql = "INSERT INTO task_acc" \
        " VALUES (null, {}, {}, {}, {}, NOW())".format(user_data['ID_Task'], user_data['id_user'], id_event, user_data['Task_point'])
    print(sql)
    try:
        gs.SqlQuery(sql)
    except:
        logging.error('error: Ошибка запроса к базе данных. Возможно такой пользователь уже есть')
        return {names.ANSWER: names.WARNING, "Data": "Ошибка запроса к базе данных."}
    return True


def check_task(data):
    sql = "SELECT ID_Task, Task_point FROM task WHERE Task_name = '{}' and Task_flag = '{}'".format(
        data['Task_name'],
        data['Task_flag'])
    print(sql)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error('Fatal error: execute database')
        return {names.ANSWER: 'Error connect db'}
    try:
        if len(result) == 2:
            result['id_user'] = data['id_user']
            input_task_acc(result)
            return {names.ANSWER: 'Success', 'Data': True}
    except:
        return {names.ANSWER: names.WARNING, 'Data': False}