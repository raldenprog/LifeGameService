# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
import api.event.show_event as show  # show_event
from api.service import GameService as gs
import api.base_name as names

class Show_all_event(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_event')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        id = args.get('id_event', None)
        try:
            answer = gs.converter(show.all_event(int(id)))
        except:
            return {names.ANSWER:names.ERROR}, 200, {'Access-Control-Allow-Origin': '*'}
        return answer, 200, {'Access-Control-Allow-Origin': '*'}