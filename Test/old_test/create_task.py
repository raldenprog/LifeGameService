# coding: utf-8
from api.task.tasks import create_one_task, create_few_tasks

def create_one_task_success():
    data = {"id": "Unchecked",
        "task_category": "Unchecked",
        "task_name": "Unchecked",
        "task_flag": "Unchecked",
        "task_description": "Unchecked",
        "task_point": "Unchecked",
        "task_hint": "Unchecked",
        "task_solve": "Unchecked",
        "task_link": "Unchecked",
        "database": "Unchecked"
        }

    print(create_one_task(data))


def create_few_tasks_success():
    data = {"id": "1",
            "task_category": "crypto",
            "task_name": "town",
            "task_flag": "1234567890",
            "task_description": "Unchecked",
            "task_point": "100",
            "task_hint": "Don't use it",
            "task_solve": "?",
            "task_link": "http://google.com"
            },{"id": "2",
        "task_category": "crypto",
        "task_name": "downtown",
        "task_flag": "0987654321",
        "task_description": "Use it",
        "task_point": "200",
        "task_hint": "No helps",
        "task_solve": "!",
        "task_link": "http://yandex.ru"
        }

    print(create_few_tasks(data))


def create_one_task_denied():
    data = {
            #"id": "Unchecked",
            "task_category": "Unchecked",
            "task_name": "Unchecked",
            "task_flag": "Unchecked",
            "task_description": "Unchecked",
            "task_point": "Unchecked",
            "task_hint": "Unchecked",
            "task_solve": "Unchecked",
            "task_link": "Unchecked",
            "database": "Unchecked"
            }

    data_1 = {
         "id": None,
        "task_category": "Unchecked",
        "task_name": "Unchecked",
        "task_flag": "Unchecked",
        "task_description": "Unchecked",
        "task_point": "Unchecked",
        "task_hint": "Unchecked",
        "task_solve": "Unchecked",
        "task_link": "Unchecked",
        "database": "Unchecked"
    }

    print(create_one_task(data))
    print(create_one_task(data_1))


def create_few_tasks_denied():
    # Первый тест для того, чтобы выявить ошибку в первом блоке, прекратить обработку
    # и вывести сообщение об ошибке, информацию об обработке каждого элемента и номер
    # ошибочного блока, в лог запишется проблемный элемент. Это может произойти в случае
    # отсутствия элемента или неверного имени JSON'a
    data = {"id": "1",
            "task_category": "crypto",
            "task_name": "town",
            # Проблемный элемент - снизу
            "tas_flag": "1234567890",
            "task_description": "Unchecked",
            "task_point": "100",
            "task_hint": "Don't use it",
            "task_solve": "?",
            "task_link": "http://google.com"
            }, {"id": "2",
                "task_category": "crypto",
                "task_name": "downtown",
                "task_flag": "0987654321",
                "task_description": "Use it",
                "task_point": "200",
                "task_hint": "No helps",
                "task_solve": "!",
                "task_link": "http://yandex.ru"
                }
    # Второй тест для того, чтобы выявить ошибку во втором блоке, прекратить обработку
    # и вывести сообщение об ошибке, информацию об обработке каждого элемента
    data_1 = {"id": "1",
            "task_category": "crypto",
            "task_name": "town",
            "task_flag": "1234567890",
            "task_description": "Unchecked",
            "task_point": "100",
            "task_hint": "Don't use it",
            "task_solve": "?",
            "task_link": "http://google.com"
            }, {"id": "2",
                "task_category": "crypto",
                "task_name": None,
                "task_flag": "0987654321",
                "task_description": "Use it",
                "task_point": "200",
                "task_hint": "No helps",
                "task_solve": "!",
                "task_link": "http://yandex.ru"
                }

    print(create_few_tasks(data))
    print(create_few_tasks(data_1))