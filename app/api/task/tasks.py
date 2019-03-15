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
                check_data[check] = names.SUCCESS
        except:
            error_flag = 1
            logging.error('Fatal error param \'%s\'' % check)

    if error_flag:
        return {names.ANSWER: names.ERROR,
                names.DATA: check_data}
    try:
        sql = "INSERT INTO task (task_category, task_name, task_flag, task_description, task_point, task_hint, task_solve, task_link, status, public_status, id_event)" \
            " VALUES (\'{task_category}\',\'{task_name}\'," \
            "\'{task_flag}\',\'{task_description}\',{task_point},\'{task_hint}\'," \
            "\'{task_solve}\', \'{task_link}\',\'{status}\',\'{public_status}\',\'{id_event}\')".format(**data)
        print(sql)
        gs.SqlQuery(sql)
        #check_data["database"] = "Recorded"
    except Exception as e:
        if e == 1062:
            return {names.ANSWER: names.WARNING,
                    names.DATA: 'Duplicate task'}
        logging.error('Fatal error: param \'sql\' can\'t create new record')
        #check_data["database"] = "Unrecorded"
        return {names.ANSWER: names.WARNING,
                names.DATA: check_data}
    if error_flag:
        return {names.ANSWER: names.ERROR,
                names.DATA: check_data}
    else:
        return {names.ANSWER: names.SUCCESS}


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
                    names.DATA: None,
                    "number": 0}
    except:
        print ("Except 1")
        logging.error('Fatal error in function \'create_few_tasks\', param \'batch_data\'')
        return {names.ANSWER: names.ERROR,
                names.DATA: None,
                "number": 0}

    try:
        for data in batch_data:
            answer = create_one_task(data)
            answers.append(answer)
    except:
        print ("Except 2")
        logging.error('Fatal error in function \'create_few_tasks\', param \'data\'')
        return {names.ANSWER: names.ERROR,
                names.DATA: None,
                "number": 0}

    return {names.ANSWER: names.SUCCESS,
            names.DATA: answers,
            "number": len(batch_data)}

json = {    names.ID :              "1",
            "task_category" :   2,
            "task_name" :       3,
            "task_flag" :       4,
            "task_description" :5,
            "task_point" :      6,
            "task_hint" :       7,
            "task_solve" :      8,
            "task_link" :       9
        },\
       {    names.ID :              "11",
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
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def get_task_event_category(event, task_category):
    sql = "SELECT id_task, task_name, task_category, event FROM task WHERE event={} AND task_category={}".format(event, task_category)

    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def get_task_event(data):
    sql = """SELECT ID_Task
 , Task_name
 , Task_category
 , Task_point
 , Task_description
 , Task_hint
 , Task_link
 , case
    when exists(
     select *
     from task_acc
     where id_event = {id_event}
       and id_user = {id_user}
       and id_task = t.id_task
    ) then True
   else False
   end as close
FROM task t
WHERE id_event = {id_event}
 and (select status from event where id_event = {id_event}) = 1
ORDER BY Task_category
 , Task_point
""".format(
        id_user=data['id_user'],
        id_event=data['id_event']
    )
    print(sql)
    try:
        result = gs.SqlQuery(sql)
        print('result: ', result[0])
        if result == []:
            print('error')
            get_task_event(data)
        return {names.ANSWER: names.SUCCESS, names.DATA: result}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR_CONNECT_DATABASE}


def check_task(data):
    data['Task_flag'] = data['Task_flag'].replace("'", "")
    sql = """
INSERT INTO task_acc (id_task, id_user, id_event, point, time)
SELECT
   t.id_task, {id_user}, {id_event}, t.task_point, current_timestamp
from task t
WHERE exists(
  select *
  from event
  where id_event = {id_event}
   and status = 1
)
and exists(
  select *
  from task task
  where task.id_task = {Task_id}
  and task.Task_flag = '{Task_flag}'
)
and exists(
  select *
  from participation
  where id_event = {id_event}
  and id_user = {id_user}
)
and t.id_task = {Task_id}
returning id

    """.format(
        id_event=data['id_event'],
        id_user=data['id_user'],
        Task_id=data['Task_id'],
        Task_flag=data['Task_flag'])

    try:
        result = gs.SqlQuery(sql)
        if result == []:
            return {names.ANSWER: "Wrong flag", names.DATA: False}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.WARNING, names.DATA: False}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}
