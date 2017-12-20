# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
import api.event.show_event as show  # show_event
from api.converter_json import converter

class Event(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        page = args.get('page', None)
        try:
            answer = converter(show.all_event(int(page)))
        except:
            return {'Answer': "Error"}, 200, {'Access-Control-Allow-Origin': '*'}
        return answer, 200, {'Access-Control-Allow-Origin': '*'}