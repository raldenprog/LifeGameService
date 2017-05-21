import logging

def check_id(id, current_connect):
    '''
    Входные параметры:
    id
    current_connect

    Выходные:
    1 OR 0

    Передаем функции искомый id и соединение с базой данных
    Получает количество id в базе и если data["id"]<= количеству, то данный id есть.
    Возвращает 1 если id есть, 0 если id нет
    '''
    try:
        sql = "SELECT id FROM users"
        current_connect.execute(sql)
        result = current_connect.fetchall()
        if len(result) >= id:
            return 1
        else:
            return 0
    except:
        logging.error('Fatal error: check id')
        return {"Answer": "Error"}
