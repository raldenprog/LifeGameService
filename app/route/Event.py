# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
import api.event.show_event as show  # show_event
import api.event.edit_event as edit
from api.service import GameService as gs
from api.event.registration_user import registration as reg_user
from api.auth.auth import session_verification
import api.base_name as names


class Event(Resource):
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
        if self.param == "find" and self.data is not None:
            answer = gs.converter(show.find_event(self.data[names.NAME], int(self.data[names.PAGE]))[names.DATA][0])
            return answer
        elif self.param == "current" and self.data is not None:
            answer = gs.converter(show.current_event(self.data[names.PAGE]))
            return answer
        elif self.param == "end" and self.data is not None:
            answer = gs.converter(show.end_event(self.data[names.PAGE]))
            return answer
        elif self.param == "registration" and self.data is not None:
            answer = gs.converter(edit.registration_event(self.data))
            return answer
        elif self.param == "update" and self.data is not None:
            answer = gs.converter(edit.update_event(self.data))
            return answer
        elif self.param == "reg_user" and self.data is not None:
            self.data["id_user"] = session_verification(self.data["UUID"])
            answer = gs.converter(reg_user(self.data))
            return answer
        elif self.param is None and self.data[names.PAGE] is not None:
            answer = gs.converter(show.all_event(self.data[names.PAGE]))
            return answer

    def get(self):
        try:
            print("Event")
            self.parse_data()
            answer = gs.converter(self.switch())
            print("answer: ", answer)
            return answer, 200, {'Access-Control-Allow-Origin': '*'}
        except:
            return "Error", 200, {'Access-Control-Allow-Origin': '*'}