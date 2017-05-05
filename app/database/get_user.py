import pymysql


def get_table(login):
    """Функция получения данных из базы, передаем ей название таблицы
    """
    try:
        connect = pymysql.connect(host='localhost', user='root', password='#', db='life_game_service',
                                  cursorclass=pymysql.cursors.DictCursor)
        cur = connect.cursor()
    except:
        #print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        return 1
    else:
        try:
            cur.execute("SELECT * FROM users where login = '{}'".format(login))
            connect.commit()
        except:
            return 1
        result = cur.fetchall()
        connect.close()
        return len(result)

