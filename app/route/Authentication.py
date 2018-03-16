# coding=utf-8

from flask_restful import Resource, reqparse
import api.auth.login_user as auth
import api.base_name as names
from api.service import GameService as gs


class Authentication(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('data')
        self.__args = self.__parser.parse_args()
        self.data = None

    def parse_data(self):
        self.data = self.__args.get('data', None)
        self.data = gs.converter(self.data)
        return

    def check_data(self):
        if self.data[names.LOGIN] is None:
            return False
        if self.data[names.PASSWORD] is None:
            return False
        return True

    def switch(self):
        answer = auth.login_verification(self.data)
        return answer

    def get(self):
        self.parse_data()
        check = self.check_data()
        if check:
            answer = self.switch()
            return answer, 200, {'Access-Control-Allow-Origin': '*'}
        return "Error",  200, {'Access-Control-Allow-Origin': '*'}
