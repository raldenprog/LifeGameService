import pymysql
import logging

logging.basicConfig(filename='logger.log',
                    format='%(asctime)s %(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s',
                    level=logging.INFO)

def db_connect():
    '''
    Функция подключается к базе данных life_game_service_database и возвращает подключение к ней
    '''
    try:
        connect = pymysql.connect(host='5.137.227.36',
                                  user='dev_life_user',
                                  password='pinlox123',
                                  db='life_game_service_database',
                                  cursorclass=pymysql.cursors.DictCursor)
        return (connect)
    except:
        logging.error('Fatal error: connect database')
        return {"Answer": "Error"}

