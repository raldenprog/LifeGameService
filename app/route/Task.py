# coding=utf-8
import json
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
import api.task.tasks as tasks
import api.auth.auth as auth
import api.base_name as names


class Task(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session')
        parser.add_argument('Task_name')
        parser.add_argument('Task_flag')
        parser.add_argument('id_event')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        session = args.get('session', None)
        Task_name = args.get('Task_name', None)
        Task_flag = args.get('Task_flag', None)
        id_event = args.get('id_event', None)
        id_user = auth.session_verification(session)
        answer = None
        if Task_name is not None and Task_flag is not None and session is not None:
            data = {'Task_name': Task_name, 'Task_flag': Task_flag, names.ID_USER: id_user, 'Task_flag': id_event}
            answer = tasks.check_task(data)
        else:
            data = {'id_event': id_event, names.ID_USER: id_user} \
                if session is not None and isinstance(id_user, int) else {'id_event': id_event, names.ID_USER: 0}
            temp = tasks.get_task_event(data)
            answer = {names.DATA: [], names.ANSWER: temp[names.ANSWER]}
            print(temp)
            for i in temp[names.DATA]:
                answer[names.DATA].append(i)
        if id is not None:
            login = auth.get_login(id_user)
            answer[names.LOGIN] = login
        return answer, 200, HEADER
