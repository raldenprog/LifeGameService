# coding=utf-8
import json
from flask_restful import Resource
from flask import request
from api.config import HEADER
from api.auth.registration_users import registration_user
import api.base_name as names


class Registration(Resource):
    def get(self):
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.args)
        return {'test': 'test'}, 200, HEADER

    def post(self):
        print('POST /registration')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.form)
        url = json.loads(request.data.decode())[names.DATA]
        print(url)
        answer = registration_user(url)
        print(answer)
        return answer, 200, {'Access-Control-Allow-Origin': '*'}

    def options(self):
        return {'Allow': 'POST'}, 200, {'Access-Control-Allow-Origin': '*',
                                        'Access-Control-Allow-Methods': 'POST,GET',
                                        'Access-Control-Allow-Headers': 'Access-Control-Allow-Origin, '
                                                                        'Content-Type, '
                                                                        'X-Custom-Header'}