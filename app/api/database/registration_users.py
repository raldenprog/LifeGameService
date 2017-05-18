import pymysql
import hashlib


def add_user(user_data):
    """
    
    """
    print(1)
    try:
        connect = pymysql.connect(host='5.137.232.44',
                                  user='dev_life_user',
                                  password='pinlox123',
                                  db='life_game_service_database',
                                  cursorclass=pymysql.cursors.DictCursor)
        current_connect = connect.cursor()
    except:
        #print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        return False
    else:
        password_hash = hashlib.md5()
        password_hash.update(user_data['password'].encode())
        user_data['password'] = password_hash.hexdigest()
        try:
            sql = "INSERT INTO users" \
                " VALUES (null,\"{login}\",\"{password}\",\"{name}\"," \
                "\"{patronymic}\",\"{email}\",\"{sex}\",\"{city}\"," \
                "\"{Educational}\",\"{logo}\", 1, 1, 1)".format(**user_data)
            print(sql)
            current_connect.execute(sql)
            connect.commit()
            connect.close()
        except:
            print('aaa')
            return False

        return True