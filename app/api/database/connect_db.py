# coding=utf-8
import pymysql
import logging

logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)

def db_connect():
    """"
    Функция подключается к базе данных life_game_service_database и возвращает подключение к ней
    """
    try:
        connect = pymysql.connect(host='localhost',
                                  user='dev_life_user',
                                  password='PINLOX!@#',
                                  db='life_game_service',
                                  cursorclass=pymysql.cursors.DictCursor)
        return connect, connect.cursor()
    except:
        logging.error('Fatal error: connect database')
        return -1, -1
