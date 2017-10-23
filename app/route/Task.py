# coding=utf-8
import json
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
import api.task.tasks as tasks
import api.auth.auth as auth


class Task(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session')
        parser.add_argument('Task_name')
        parser.add_argument('Task_flag')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        session = args.get('session', None)
        Task_name = args.get('Task_name', None)
        Task_flag = args.get('Task_flag', None)
        session = session[0] if session is not None else None
        Task_name = Task_name[0] if Task_name is not None else None
        Task_flag = Task_flag[0] if Task_flag is not None else None
        id_user = auth.session_verification(session)
        answer = None
        if Task_name is not None and Task_flag is not None and session is not None:
            data = {'Task_name': Task_name, 'Task_flag': Task_flag, 'id_user': id_user}
            answer = tasks.check_task(data)
        else:
            data = {'id_event': 1, 'id_user': id_user} \
                if session is not None and isinstance(id_user, int) else {'id_event': 1, 'id_user': 0}
            answer = tasks.get_task_event(data)
        login = auth.get_login(id_user)
        answer['Login'] = login
        return answer, 200, HEADER
