# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
from api.user_cabinet.cabinet import edit_cabinet
from api.user_cabinet.cabinet import user_cabinet
import api.base_name as names
from api.service import GameService as gs

class Cabinet(Resource):
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
        print(self.param)
        print(self.data)
        self.data = gs.converter(self.data)
        return
    def switch(self):
        print(self.param)
        if self.param == "edit" and self.data is not None:
            answer = edit_cabinet(self.data)
        else:
            answer = user_cabinet(self.data)
        return answer

    def get(self):
        self.parse_data()
        answer = self.switch()
        return answer, 200, {'Access-Control-Allow-Origin': '*'}
#        return "Error", 200, {'Access-Control-Allow-Origin': '*'}