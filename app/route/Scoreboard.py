# coding=utf-8
import json
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
import api.scoreboard.get_scoreboard as score


class Scoreboard(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session', action='append')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        answer = score.get_scoreboard()
        print(answer)
        return answer, 200, HEADER
