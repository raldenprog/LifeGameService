# coding=utf-8
import json
import sys
import os
sys.path.append(os.getcwd())
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from route.registration import Registration
from route.Authentication import Authentication
from route.Task import Task
from route.Logout import Logout
from route.Scoreboard import Scoreboard
from route.Event import Event

_app = Flask(__name__)
_app.config['JSON_AS_ASCII'] = False
api = Api(_app)
HEADER = {'Access-Control-Allow-Origin': '*'}


@_app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404


class index(Resource):
    def get(self):
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.args)
        return {'test': 'test'}, 200, HEADER


api.add_resource(Registration, '/registration')
api.add_resource(Authentication, '/auth')
api.add_resource(Task, '/task')
api.add_resource(Scoreboard, '/scoreboard')
api.add_resource(Logout, '/logout')
api.add_resource(index, '/')
api.add_resource(Event, '/event')


if __name__ == '__main__':
    try:
        _app.run(host='0.0.0.0', port='13451', threaded=True)
    except Exception as e:
        print(e)
