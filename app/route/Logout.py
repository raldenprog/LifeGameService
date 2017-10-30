# coding=utf-8
import json
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
import api.auth.login_user as auth


class Logout(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('session')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        session = args.get('session')
        auth.logout_user(session)
        return {'Answer': 'Success'}, 200, HEADER
