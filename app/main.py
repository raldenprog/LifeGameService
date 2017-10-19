# coding=utf-8
from flask import Flask, request
from flask_restful import Resource, Api
import api.auth.login_user as auth
import json
from api.auth.registration_users import registration_user

_app = Flask(__name__)
api = Api(_app)

HEADER = {'Access-Control-Allow-Origin': '*'}


@_app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404

class registration(Resource):
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
        url = json.loads(request.form['Data'])
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


class authentication(Resource):
    def get(self):
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.form)
        return {'test': 'test'}, 200, HEADER

    def post(self):
        print('POST /auth')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.form)
        url = json.loads(request.form['Data'])
        print(url)
        answer = auth.login_verification(url)
        print(answer)
        return answer, 200, {'Access-Control-Allow-Origin': '*'}

    def options(self):
        return {'Allow': 'POST'}, 200, {'Access-Control-Allow-Origin': '*',
                                        'Access-Control-Allow-Methods': 'POST,GET',
                                        'Access-Control-Allow-Headers': 'Access-Control-Allow-Origin, '
                                                                        'Content-Type, '
                                                                        'X-Custom-Header'}

class index(Resource):
    def get(self):
        print('GET /')
        print(request.headers)
        print('cookies = ', request.cookies)
        print('ARGS = ', request.args)
        return {'test': 'test'}, 200, HEADER

api.add_resource(registration, '/registration')
api.add_resource(authentication, '/auth')
api.add_resource(index, '/')


if __name__ == '__main__':
    try:
        _app.run(host='0.0.0.0', port='13451', threaded=True)
    except Exception as e:
        print(e)
