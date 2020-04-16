# coding=utf-8
import logging
import psycopg2
from psycopg2.extras import RealDictCursor
from api.config import DATABASE
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


def db_connect_new():
    connect = psycopg2.connect("dbname='{dbname}' user='{user}' host='{host}' password='{password}'".format(**DATABASE))
    return connect, connect.cursor(cursor_factory=RealDictCursor)