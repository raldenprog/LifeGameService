# coding=utf-8
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/api')
sys.path.append(os.getcwd()+'/route')
from flask import Flask
from flask_restful import Api
import api.base_name as names
from route import Registration, \
    Authentication, \
    Task, \
    Logout, \
    Scoreboard, \
    Event, \
    Cabinet, \
    Index, \
    Favicon, \
    News

routes = {Index.Index: '/',
          Registration.Registration: '/registration',
          Authentication.Authentication: '/auth',
          Task.Task: '/task',
          Scoreboard.Scoreboard: '/scoreboard',
          Event.Event: '/event',
          Cabinet.Cabinet: '/cabinet',
          Logout.Logout: '/logout',
          Favicon.Favicon: "/favicon.ico",
          News.News: "/news",
          News.Comment: "/comment"
          }

_app = Flask(__name__)
_app.config['JSON_AS_ASCII'] = False
api = Api(_app)
HEADER = {'Access-Control-Allow-Origin': '*'}


@_app.errorhandler(404)
def not_found(error):
    return {names.ERROR: 'Not found'}, 404


if __name__ == '__main__':

    try:
        for route_class, route in routes.items():
            api.add_resource(route_class, route)
        _app.run(host='0.0.0.0', port=13451, threaded=True, debug=True)
    except Exception as e:
        print(e)
