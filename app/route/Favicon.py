__author__ = 'RaldenProg'
# coding=utf-8

from flask_restful import Resource, reqparse


class Favicon(Resource):
    def get(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}