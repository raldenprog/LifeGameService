import logging


"""
action:
    login
    registration
    scoreboard
    cabinet
    command
    task
    add_Task
"""

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def func(data):
    try:
        if data["name"] is not None:
            print(data["name"])
        else:   # Если не верно задан логин (Это пример, условие должно быть другим)
            logging.info('Incorrect parameter \'name\'')
            return {"answer": "Error"}
    except:
        logging.error('Fatal error in function fun, param \'name\'')
        return {"answer": "Error"}
    try:
        if data["id"] is not None:
            print(data["id"])
        else: # Если не верно задан id (Это пример, условие должно быть другим)
            logging.info('Incorrect parameter \'name\'')
            return {"answer": "Error"}
    except:
        logging.error('Fatal error in function fun, param \'id\'')
        return {"answer": "Error"}

    return {"answer": "Ok",
            "data": {
                "name": "Anton",
                "id": 13
                }
            }


def f():
    ans = {
        "action": "login",
        "data": {
            "name": "Anton"
        }
    }
    ans = func(ans["data"])
    print(ans)
f()
