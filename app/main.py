import logging
import json
import threading
import os
from app.Server import Server
from app.api.database.registration_users import add_user
from app.api.database.login_user import login_verification
from werkzeug.wsgi import SharedDataMiddleware

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


def func1(data, writer):
    print('func1 -> ', data)
    data = login_verification(data)
    print(data)
    data = json.dumps(data)
    writer.send(data.encode())
    writer.close()


def func2(data, writer):
    print('func2 -> ', data)
    data = add_user(data)
    print(data)
    data = json.dumps(data)
    writer.send(data.encode())
    writer.close()


def quest(data, conn):
    print('Action = ', data['Action'])
    if data['Action'] == 'Add_user':
        thread = threading.Thread(target=func1, args=(data['Data'], conn))
    elif data['Action'] == 'Registration_user':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Update_event':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Scoreboard_all_user':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Scoreboard_event_users':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_create_one_task':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_create_few_tasks':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_get_task_event_name':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_get_task_event_category':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'User_cabinet':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Change_password':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Edit_cabinet':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    else:
        ans = {"Error": "Action error"}
    thread.start()


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Server({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=False, use_reloader=True)