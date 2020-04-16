# coding=utf-8
import json
from flask_restful import Resource, reqparse
import api.task.tasks as tasks
import api.base_name as names
from api.service import GameService as gs
from api.auth.auth import session_verification


class Task(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('data')
        self.__parser.add_argument('param')
        self.__args = self.__parser.parse_args()
        self.data = None
        self.param = None

    def parse_data(self):
        self.data = self.__args.get('data', None)
        self.param = self.__args.get('param', None)
        print("param: ", self.param)
        print("data: ", self.data)
        self.data = gs.converter(self.data)

        return

    def switch(self):
        if self.data is not None and self.param == "check":
            self.data["id_user"] = session_verification(self.data["UUID"])
            answer = tasks.check_task(self.data)
            return answer
        if self.data is not None and self.param == "create":
            print(1)
            answer = tasks.create_one_task(self.data)
            return answer
        elif self.data is not None:
            self.data["id_user"] = session_verification(self.data["UUID"])
            answer = tasks.get_task_event(self.data)
            print('ans:', answer)
            return answer

    def get(self):
        print("Task")
        self.parse_data()
        answer = self.switch()
        print("answer: ", answer)
        return answer, 200, {'Access-Control-Allow-Origin': '*'}