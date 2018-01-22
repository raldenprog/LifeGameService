# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
from api.user_cabinet.cabinet import edit_cabinet
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

        param = args.get('param', None)
        try:
            if param == "edit" and id_user is not None:
                answer = edit_cabinet({names.ID_USER: id_user})
                return answer, 200, {'Access-Control-Allow-Origin': '*'}
        except:
            return {names.ANSWER: names.ERROR}, 200, {'Access-Control-Allow-Origin': '*'}
        return answer, 200, {'Access-Control-Allow-Origin': '*'}