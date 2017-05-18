import pymysql


def get_table(login):
    """
    
    """
    try:
        connect = pymysql.connect(host='5.137.232.44',
                                  user='dev_life_user',
                                  password='pinlox123',
                                  db='life_game_service_database',
                                  cursorclass=pymysql.cursors.DictCursor)
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

