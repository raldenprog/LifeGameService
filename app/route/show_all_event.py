# coding=utf-8
import json
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
import api.event.show_event as show  # show_event
from api.converter_json import converter
class show_all_event(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_event')
        args = parser.parse_args()
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', args)
        id = args.get('id_event', None)
        """
        if id is not None:
            show_id = int(json.loads(request.data.decode())['id_event'])
            answer = show.all_event(show_id)
        else:
            answer = show.all_event(0)
        """
        answer = show.all_event(0)
        answer = converter(answer)
        print("Show_all_event_ answer == ", answer)
        return answer, 200, {'Access-Control-Allow-Origin': '*'}

#show_all_event.get(0)