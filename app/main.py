import json
import logging
import os
import threading

from werkzeug.wsgi import SharedDataMiddleware

from app.Server import Server
from app.api.auth.login_user import login_verification
from app.api.auth.registration_users import add_user

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


# TODO: отсюда будет расходиться логика
def quest(data, conn):
    print('Action = ', data['Action'])
    if data['Action'] == 'Add_user':
        pass
    elif data['Action'] == 'Registration_user':
        pass
    elif data['Action'] == 'Update_event':
        pass
    elif data['Action'] == 'Scoreboard_all_user':
        pass
    elif data['Action'] == 'Scoreboard_event_users':
        pass
    elif data['Action'] == 'Task_create_one_task':
        pass
    elif data['Action'] == 'Task_create_few_tasks':
        pass
    elif data['Action'] == 'Task_get_task_event_name':
        pass
    elif data['Action'] == 'Task_get_task_event_category':
        pass
    elif data['Action'] == 'User_cabinet':
        pass
    elif data['Action'] == 'Change_password':
        pass
    elif data['Action'] == 'Edit_cabinet':
        pass
    else:
        ans = {"Error": "Action error"}


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