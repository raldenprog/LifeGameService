# coding=utf-8
from flask_restful import Resource, reqparse
from api.service import GameService as gs


class BaseRoute(Resource):
    def __init__(self):
        self.arguments = []
        self.parser = reqparse.RequestParser()

    def parse_data(self):
        self.data = gs.converter(self.data)
        return

    def switch(self):
        pass

    def get(self):
        pass
        # return , 200, {'Access-Control-Allow-Origin': '*'}
