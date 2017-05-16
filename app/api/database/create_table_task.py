import pymysql


def create_table_task(name):
    """
    
    """
    try:
        connect = pymysql.connect(host='localhost', user='root', password='#', db='life_game_service',
                                  cursorclass=pymysql.cursors.DictCursor)
    except:
        return False

    sql = "CREATE TABLE {} (" \
        "id int(11) NOT NULL AUTO_INCREMENT," \
        "task_category varchar(30) NOT NULL," \
        "task_name varchar(255) NOT NULL," \
        "task_flag varchar(255) NOT NULL," \
        "task_description varchar(2048) NOT NULL,"\
        "task_point int(4) NOT NULL," \
        "task_hint varchar(1024) NOT NULL," \
        "task_solve varchar(1024) NOT NULL," \
        "task_link varchar(512) NOT NULL," \
        "PRIMARY KEY (id)" \
        ") " \
        "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;".format(name)
    print(sql)
    try:
        current_connect = connect.cursor()
        current_connect.execute(sql)
        current_connect.close()
    except:
        return False
    return True

