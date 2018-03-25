# coding=utf-8
import api.base_name as names
import logging
from api.database.connect_db import db_connect_new
import datetime
from api.service import GameService as gs
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def comment_verification(comment_data):
    """
    Метод проверяет корректность параметров
    :param comment_data: dict хранит информацию о комментарии
    :return: id_comment
    """
    check = [names.COMMENT, names.ID_USER, names.ID_COMMENT_PARENT, names.ID_NEWS]
    error = False
    for data in check:
        if comment_data.get(data, None) is None:
            logging.info('Incorrect parameter ' + data)
            comment_data[data] = 'Пустой параметр!'
            error = True
    if error:
        return {names.ANSWER: names.ERROR, names.DATA: comment_data}

    comment_data[names.DISLIKES_COUNT] = 0
    comment_data[names.LIKES_COUNT] = 0
    comment_data[names.DATA] = datetime.datetime.now()

    answer = input_comments_table(comment_data)
    if answer.get(names.ANSWER) is not names.SUCCESS:
        return {names.ANSWER: names.WARNING, names.DATA: "Ошибка запроса к базе данных"}
    return answer


def input_comments_table(comment_data):
    """
    Метод добавляет комментарий в БД
    :param comment_data: dist хранит информацию о комментарии
    :return: id_comment
    """
    connect, current_connect = db_connect_new()
    if connect == -1:
        return {names.ANSWER: names.WARNING, names.DATA: "Ошибка доступа к базе данных, повторить позже"}
    sql = "INSERT INTO Comments (id_news, id_comment_parent, Comment_text, id_user, Likes_count, Dislikes_count, Data)" \
          " VALUES (\'{id_news}\', \'{id_comment_parent}\', \'{Comment_text}\', \'{id_user}\', \'{Likes_count}\', " \
          "\'{Dislikes_count}\', \'{Data}\')" \
          "RETURNING id_comment"\
        .format(id_news=comment_data.get(names.ID_NEWS),
                id_comment_parent=comment_data.get(names.ID_COMMENT_PARENT),
                Comment_text=comment_data.get(names.COMMENT),
                id_user=comment_data.get(names.ID_USER),
                Likes_count=comment_data.get(names.LIKES_COUNT),
                Dislikes_count=comment_data.get(names.DISLIKES_COUNT),
                Data=comment_data.get(names.DATA))
    try:
        id_comment = gs.SqlQuery(sql)[0]['id_comment']
    except:
        logging.error('error: Ошибка запроса к базе данных. Возможно такой комментарий уже есть')
        return {names.ANSWER: names.WARNING,
                names.DATA: "Ошибка запроса к базе данных. Возможно такой комментарий уже есть"}
    return id_comment
