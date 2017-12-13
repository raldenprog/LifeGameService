__author__ = 'ar.chusovitin'
import json
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../app/api')
sys.path.append(os.getcwd()+'/../app/route')
import unittest
import requests as req
from app.api.sql import SqlQuery
from app.api.database.connect_db import db_connect_new as db

#URL = 'http://127.0.0.1:13451'
#URL = 'http://87.103.243.110:13451'


class TestRegistration(unittest.TestCase):

    def test_connect(self):
        try:
            connect, current_connect = db()
        except Exception as e:
            print(e)

    def test_query(self):
        sql_query = ["""CREATE TABLE test (coltest varchar(20));""",
                 """insert into test (coltest) values ('It works!');""",
                 """SELECT EXISTS (SELECT 1 from test);""",
                 """DROP TABLE test;"""]
        for i in range(2):
            try:
                SqlQuery(sql_query[i])
            except:
                raise
        result = SqlQuery(sql_query[2])
        SqlQuery(sql_query[3])
        self.assertEqual(result[0][0], True)

    def test_users_query(self):
        sql = """SELECT * FROM users;"""
        result = SqlQuery(sql)
        print(result)
