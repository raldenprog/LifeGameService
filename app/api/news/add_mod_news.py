# coding=utf-8
import logging
import api.base_name as names
from api.database.connect_db import db_connect_new
import datetime
from api.service import GameService as gs
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def news_verification(news_data):
    """
    Метод проверяет корректность параметров
    :param news_data: dict хранит информацию о новости
    :return: id_news
    """
    # TODO: Проверить права на добавление новости
    check = [names.ID_USER, names.NEWS]
    error = False
    for data in check:
        if news_data.get(data, None) is None:
            logging.info('Incorrect parameter ' + data)
            news_data[data] = 'Пустой параметр!'
            error = True
    if error:
        return {names.ANSWER: names.ERROR, names.DATA: news_data}

    news_data[names.DISLIKES_COUNT] = 0
    news_data[names.LIKES_COUNT] = 0
    news_data[names.DATA] = datetime.datetime.now()

    answer = input_news_table(news_data)
    if answer.get(names.ANSWER) is not names.SUCCESS:
        return {names.ANSWER: names.WARNING, names.DATA: "Ошибка запроса к базе данных"}
    return answer


def input_news_table(news_data):
    """
    Метод добавляет новость в БД
    :param news_data: dist данные о новости
    :return: id_news
    """
    connect, current_connect = db_connect_new()
    if connect == -1:
        return {names.ANSWER: names.WARNING, names.DATA: "Ошибка доступа к базе данных, повторить позже"}
    sql = "INSERT INTO News (News_text, id_user, Likes_count, Dislikes_count, Data)" \
          " VALUES (\'{News_text}\',\'{id_user}\',\'{Likes_count}\',\'{Dislikes_count}\',\'{Data}\') " \
          "RETURNING id_news"\
        .format(News_text=news_data.get(names.NEWS),
                id_user=news_data.get(names.ID_USER),
                Likes_count=news_data.get(names.LIKES_COUNT),
                Dislikes_count=news_data.get(names.DISLIKES_COUNT),
                Data=news_data.get(names.DATA))
    try:
        id_news = gs.SqlQuery(sql)[0]['id_news']
    except:
        logging.error('error: Ошибка запроса к базе данных. Возможно такая новость уже есть')
        return {names.ANSWER: names.WARNING,
                names.DATA: "Ошибка запроса к базе данных. Возможно такая новость уже есть"}
    return id_news


def get_news_by_id_user(id_user):
    sql = "SELECT * FROM News n WHERE n.id_user = {id_user} ORDER BY n.Data"\
        .format(id_user=id_user)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: 'Error connect db'}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def get_news_order_by_data():
    sql = "SELECT * FROM News n ORDER BY n.Data"
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: 'Error connect db'}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}
