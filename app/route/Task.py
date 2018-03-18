# coding=utf-8
import json
from flask_restful import Resource, reqparse
import api.task.tasks as tasks
import api.base_name as names
from api.service import GameService as gs


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
        self.data = gs.converter(self.data)
        return

    def switch(self):
        print(self.data)
        if self.data is not None and self.param == "check":
            answer = tasks.check_task(self.data)
            print(answer)
            return answer
        elif self.data is not None:
            answer = tasks.get_task_event(self.data)
            print(answer)
            return answer

    def get(self):
        self.parse_data()
        answer = self.switch()
        return answer, 200, {'Access-Control-Allow-Origin': '*'}
#        return "Error", 200, {'Access-Control-Allow-Origin': '*'}
