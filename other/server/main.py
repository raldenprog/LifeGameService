# coding: utf8
import logging
import os

from werkzeug.wsgi import SharedDataMiddleware

from other.server.Server import Server

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Server({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('0.0.0.0', 13451, app, use_debugger=False, use_reloader=True)