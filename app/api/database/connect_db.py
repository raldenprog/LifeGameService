# coding=utf-8
import psycopg2
from psycopg2.extras import RealDictCursor
from api.config import DATABASE


def db_connect_new():
    connect = psycopg2.connect("dbname='{dbname}' user='{user}' host='{host}' password='{password}'".format(**DATABASE))
    return connect, connect.cursor(cursor_factory=RealDictCursor)