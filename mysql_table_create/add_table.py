import pymysql

def create_table_user():
    connect = pymysql.connect(host='localhost', user='root', password='#', db='life_game_service',
                              cursorclass=pymysql.cursors.DictCursor)

    sql = "CREATE TABLE users (" \
            "id int(11) NOT NULL AUTO_INCREMENT," \
            "login varchar(30) NOT NULL," \
            "password varchar(40) NOT NULL," \
            "name varchar(30) NOT NULL," \
            "patronymic varchar(30) NOT NULL,"\
            "email varchar(50) NOT NULL," \
            "sex varchar(6) NOT NULL," \
            "city varchar(50) NOT NULL," \
            "Educational varchar(255) NOT NULL," \
            "logo varchar(255) NOT NULL," \
            "is_admin int(1) NOT NULL," \
            "is_captain int(1) NOT NULL," \
            "is_moderator int(1) NOT NULL," \
          "PRIMARY KEY (id)" \
          ") " \
          "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    current_connect = connect.cursor()
    current_connect.execute(sql)
    current_connect.close()


create_table_user()