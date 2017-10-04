import redis
import os
import json
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
import app.api.auth.login_user as auth
import app.api.auth.registration_users as registration_user


class Server(object):
    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/registration', endpoint='registration'),
        ])

    def on_index(self, request):
        error = None
        url = ''
        r = {
            'a': 10,
            'b': 15,
            'c': [
                1, 2, 3, 4, 5, 6
            ],
            'd': {
                'a': 1
            }
        }
        if request.method == 'POST':
            url = json.loads(request.form['data'])
            print(url)
        elif request.method == 'ADD':
            pass
        elif request.method == 'DELETE':
            pass
        elif request.method == 'UPDATE':
            pass

        return Response(json.dumps(r))

    def on_registration(self, request):
        error = None
        url = ''
        answer = dict()
        if request.method == 'POST':
            url = json.loads(request.form['data'])
            print(url)
            answer = auth.login_verification(url)
            print(answer)
        elif request.method == 'ADD':
            pass
        elif request.method == 'DELETE':
            pass
        elif request.method == 'UPDATE':
            pass
        return Response(json.dumps(answer))

    def error_404(self):
        status_code = 404
        return status_code

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except NotFound:
            return self.error_404()
        except HTTPException:
            return

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)