# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
import api.event.show_event as show  # show_event
from api.Converter_json import converter

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
        print("id = ", id)
        try:
            answer = converter(show.all_event(int(id)))
        except:
            return {'Answer':"Error"}, 200, {'Access-Control-Allow-Origin': '*'}
        return answer, 200, {'Access-Control-Allow-Origin': '*'}