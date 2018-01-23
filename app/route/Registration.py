# coding=utf-8
import json
from flask_restful import Resource
from flask import request
from api.config import HEADER
from api.auth.registration_users import registration_user
import api.base_name as names


class Registration(Resource):
    def get(self):
        print('GET /registration')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.args)
        data = args.get(names.DATA, None)
        answer = registration_user(data)
        return answer, 200, {'Access-Control-Allow-Origin': '*'}