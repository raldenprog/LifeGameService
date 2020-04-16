# coding=utf-8

from flask_restful import Resource, reqparse
import api.auth.login_user as auth
import api.base_name as names
from api.service import GameService as gs
from api.auth.auth import session_verification


class Authentication(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('data')
        self.__parser.add_argument('param')
        self.__args = self.__parser.parse_args()
        self.data = None

    def parse_data(self):
        self.data = self.__args.get('data', None)
        self.param = self.__args.get('param', None)
        print("param:", self.param)
        self.data = gs.converter(self.data)
        print("data: ", self.data)
        return

    def switch(self):
        if self.param == "get_user_name" and self.data is not None:
            self.data["id_user"] = session_verification(self.data["UUID"])
            print(self.data["id_user"])
            answer = gs.converter(gs.converter(auth.get_user_name(self.data["id_user"])))
            return answer
        else:
            answer = auth.login_verification(self.data)
            return answer

    def get(self):
        print("Auth")
        self.parse_data()

        answer = self.switch()
        print("answer: ", answer)
        return answer, 200, {'Access-Control-Allow-Origin': '*'}
