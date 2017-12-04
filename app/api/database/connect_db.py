# coding=utf-8
import pymysql
import logging
import psycopg2

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


def db_connect():
    """"
    Функция подключается к базе данных life_game_service_database и возвращает подключение к ней
    """
    try:
        connect = pymysql.connect(host='90.189.132.25',
                                  user='dev_life_user',
                                  password='PINLOX!@#',
                                  db='life_game_service',
                                  cursorclass=pymysql.cursors.DictCursor,
                                  charset='utf8')
        return connect, connect.cursor()
    except:
        logging.error('Fatal error: connect database')
        return -1, -1


def db_connect_new():
    try:
        connect = psycopg2.connect("dbname='life_game_service' user='life_dev' host='90.189.132.25' password='PINLOX!@#'")
        return connect, connect.cursor()
    except:
        logging.error('Fatal error: connect database')
        raise