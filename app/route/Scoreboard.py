# coding=utf-8
import json
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
import api.scoreboard.get_scoreboard as score
import api.auth.auth as auth


class Scoreboard(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session')
        args = parser.parse_args()
        session = args.get('session', None)
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        answer = score.get_scoreboard()
        try:
            id_user = auth.session_verification(session)
            login = auth.get_login(id_user)
            answer['Login'] = login
        except:
            pass
        print(answer)
        return answer, 200, HEADER
