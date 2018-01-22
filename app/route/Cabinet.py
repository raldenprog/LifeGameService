# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
from api.user_cabinet.cabinet import user_cabinet
import api.base_name as names


class Cabinet(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(names.ID)
        args = parser.parse_args()
        print('GET /cabinet')
        id_user = args.get(names.ID, None)
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.form)
        answer = user_cabinet({names.ID_USER : id_user})
        print(answer)
        return answer, 200, HEADER