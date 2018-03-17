__author__ = 'ar.chusovitin'
import json
import logging
from datetime import date
from api.database.connect_db import db_connect_new as db
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


class GameService:
    @staticmethod
    def SqlQuery(query):
        """
        Метод выполняет SQL запрос к базе
        :param query: str SQL запрос
        :return: dict результат выполнения запроса
        """
        connect, current_connect = db()
        result = None
        try:
            #print(query)
            current_connect.execute(query)
            connect.commit()
        except:
            return result
        finally:
            try:
                result = current_connect.fetchall()
            except:
                return result
            connect.close()
            return result

    @staticmethod
    def __converter_data(param):
        if isinstance(param, date):
            return param.strftime('%d.%m.%Y')

    @staticmethod
    def converter(js):
        """
        Метод преобразовывает передаваемый json в Dict и наоборот
        :param js: str или json
        :return: str или dict преобразованный элемент
        """
        return json.dumps(js, default=GameService.__converter_data) if isinstance(js, dict) \
            else json.loads(js)

    @staticmethod
    def check_id(id_user):
        """
        Передаем функции искомый id.
        Возвращает True если id есть, False если id нет
        """
        try:
            sql = "select exists(select 1 from users where id_user = {})".format(id_user)
            return GameService.SqlQuery(sql)[0]['exists']
        except:
            logging.error('Fatal error: check id')
            return {names.ANSWER: names.ERROR}