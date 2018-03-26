# coding=utf-8

from flask_restful import Resource, reqparse
from api.service import GameService as gs
import api.news.add_mod_news as news_api
import api.news.add_mod_comments as comments_api
import api.base_name as names
__author__ = 'den-isk1995'


class News(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('data')
        self.__parser.add_argument('param')
        self.__args = self.__parser.parse_args()
        self.data = None
        self.param = None

    def parse_data(self):
        self.data = self.__args.get('data', None)
        self.param = self.__args.get('param', None)
        if self.data is None and self.param is None:
            return
        self.data = gs.converter(self.data)
        print("param: ", self.param)
        print("data: ", self.data)
        return

    def check_data(self):
        if self.data is not None and self.param == "create":
            if self.data[names.NEWS] is None:
                return False
            if self.data[names.ID_USER] is None:
                return False
        return True

    def switch(self):
        if self.data is not None and self.param == "create":
            answer = news_api.news_verification(self.data)
            return answer
        else:
            answer = gs.converter(gs.converter(news_api.get_news_order_by_data()))
            return answer

    def get(self):
        try:
            print("News")
            self.parse_data()
            check = self.check_data()
            if check:
                answer = self.switch()
                print("answer: ", answer)
                return answer, 200, {'Access-Control-Allow-Origin': '*'}
            return "Error",  200, {'Access-Control-Allow-Origin': '*'}
        except:
            return "Error", 200, {'Access-Control-Allow-Origin': '*'}


class Comment(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('data')
        self.__args = self.__parser.parse_args()
        self.data = None

    def parse_data(self):
        self.data = self.__args.get('data', None)
        self.data = gs.converter(self.data)
        print("data: ", self.data)
        return

    def check_data(self):
        if self.data[names.COMMENT] is None:
            return False
        if self.data[names.ID_USER] is None:
            return False
        if self.data[names.ID_COMMENT_PARENT] is None:
            return False
        if self.data[names.ID_NEWS] is None:
            return False
        return True

    def switch(self):
        answer = comments_api.comment_verification(self.data)
        return answer

    def get(self):
        try:
            print("Comment")
            self.parse_data()
            check = self.check_data()
            if check:
                answer = self.switch()
                print("answer: ", answer)
                return answer, 200, {'Access-Control-Allow-Origin': '*'}
            return "Error",  200, {'Access-Control-Allow-Origin': '*'}
        except:
            return "Error", 200, {'Access-Control-Allow-Origin': '*'}
