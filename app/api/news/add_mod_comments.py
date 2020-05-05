# coding=utf-8
import api.base_name as names
from api.service import GameService as gs


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
            comment_data[data] = 'Пустой параметр!'
            error = True
    if error:
        return {names.ANSWER: names.ERROR, names.DATA: comment_data}

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
    sql = """INSERT INTO Comments (id_news, id_comment_parent, Comment_text, id_user, Likes_count, Dislikes_count, Date)
          VALUES ({id_news}, {id_comment_parent}, '{Comment_text}', {id_user}, 0, 0, current_timestamp)
          RETURNING id_comment
          """.format(id_news=comment_data[names.ID_NEWS],
                     id_comment_parent=comment_data[names.ID_COMMENT_PARENT],
                     Comment_text=comment_data[names.COMMENT],
                     id_user=comment_data[names.ID_USER])
    id_comment = gs.SqlQuery(sql)[0]['id_comment']
    return {names.ANSWER: names.SUCCESS, names.DATA: {"id_comment": str(id_comment)}}


def get_comments_by_id_news(id_news):
    """
     Метод извлекает все комментарии по id_news
    :param id_news: ID новости для которой извлекаются комментарии
    :return: dict
    """
    sql = "SELECT * FROM Comments c WHERE c.id_news = {id_news} ORDER BY c.id_comment_parent".format(id_news=id_news)
    result = gs.SqlQuery(sql)
    return {names.ANSWER: names.SUCCESS, names.DATA: result}
