# coding=utf-8
from flask import Flask
from flask_restful import Api
import api.base_name as names
from route import routes


_app = Flask(__name__)
_app.config['JSON_AS_ASCII'] = False
api = Api(_app)
HEADER = {'Access-Control-Allow-Origin': '*'}


@_app.errorhandler(404)
def not_found(error):
    return {names.ERROR: 'Not found'}, 404


if __name__ == '__main__':
    for route_class, route in routes.items():
        api.add_resource(route_class, route)
    _app.run(host='0.0.0.0', port=13451, threaded=True, debug=True)
