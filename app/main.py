from flask import Flask, request
from flask_restful import Resource, Api
import api.auth.login_user as auth
import json
from api.auth.registration_users import registration_user

_app = Flask(__name__)
api = Api(_app)

HEADER = {'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization',
          'Access-Control-Allow-Methods': 'GET,POST'}

class registration(Resource):
    def get(self):
        return {'test': 'test'}, 200, HEADER

    def post(self):
        print(1)
        url = json.loads(request.form['Data'])
        answer = registration_user(url)
        return answer, 200, HEADER


class authentication(Resource):
    def get(self):
        return {'test': 'test'}, 200, HEADER

    def post(self):
        url = json.loads(request.form['Data'])
        print(url)
        answer = auth.login_verification(url)
        print(answer)
        return answer, 200, HEADER


api.add_resource(registration, '/registration')  # Route_1
api.add_resource(authentication, '/auth')  # Route_2


if __name__ == '__main__':
    try:
        _app.run(host='127.0.0.1', port='13451', threaded=True)
    except Exception as e:
        print(e)
