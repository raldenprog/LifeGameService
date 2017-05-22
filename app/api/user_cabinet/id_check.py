import logging


logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def check_id(id_user, current_connect):
    """
    Входные параметры:
    id
    current_connect

    Выходные:
    1 OR 0

    Передаем функции искомый id и соединение с базой данных
    Получает количество id в базе и если data["id"]<= количеству, то данный id есть.
    Возвращает 1 если id есть, 0 если id нет
    """
    try:
        sql = "SELECT * FROM users where id = '{}'".format(id_user)
        current_connect.execute(sql)
        result = current_connect.fetchall()[0]
        if len(result['password']) != 0:
            return 1
        else:
            return 0
    except:
        logging.error('Fatal error: check id')
        return {"Answer": "Error"}
