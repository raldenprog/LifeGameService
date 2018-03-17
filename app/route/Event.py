# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
import api.event.show_event as show  # show_event
from api.service import GameService as gs
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
        elif self.param is None and self.data[names.PAGE] is not None:
            answer = gs.converter(show.all_event(self.data[names.PAGE]))
            return answer

    def get(self):
        try:
            self.parse_data()
            answer = self.switch()
            return answer, 200, {'Access-Control-Allow-Origin': '*'}
        except:
            return "Error", 200, {'Access-Control-Allow-Origin': '*'}