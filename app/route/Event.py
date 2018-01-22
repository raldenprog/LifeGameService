# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
import api.event.show_event as show  # show_event
from api.service import GameService as gs
import api.base_name as names
from api.event.show_event import find_event


class Event(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page')
        parser.add_argument('param')
        parser.add_argument('name')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        page = args.get('page', None)
        param = args.get('param', None)
        name = args.get('name', None)
        try:
            if param == "find" and name is not None:
                answer = gs.converter(find_event(name, int(page)))
                return answer, 200, {'Access-Control-Allow-Origin': '*'}
            else:
                answer = gs.converter(show.all_event(int(page)))
        except:
            return {names.ANSWER: names.ERROR}, 200, {'Access-Control-Allow-Origin': '*'}
        return answer, 200, {'Access-Control-Allow-Origin': '*'}
