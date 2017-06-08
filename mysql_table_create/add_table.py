import pymysql
from app.api.database.connect_db import db_connect

def create_table_user():

    connect, current_connect = db_connect()

    sql = "CREATE TABLE Users (" \
        "ID int(11) NOT NULL AUTO_INCREMENT," \
        "Login varchar(30) NOT NULL," \
        "Password varchar(40) NOT NULL," \
        "Name varchar(30) NOT NULL," \
        "Patronymic varchar(30) NOT NULL,"\
        "Email varchar(50) NOT NULL," \
        "Sex varchar(6) NOT NULL," \
        "City varchar(50) NOT NULL," \
        "Educational varchar(255) NOT NULL," \
        "Logo varchar(255) NOT NULL," \
        "is_admin int(1) NOT NULL," \
        "is_captain int(1) NOT NULL," \
        "is_moderator int(1) NOT NULL," \
        "PRIMARY KEY (id)" \
        ") " \
        "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_event():
    connect, current_connect = db_connect()

    sql = "CREATE TABLE Event (" \
        "ID int(11) NOT NULL AUTO_INCREMENT," \
        "Name varchar(255) NOT NULL," \
        "Description varchar(2048) NOT NULL," \
        "Logo varchar(30) NOT NULL," \
        "Status varchar(30) NOT NULL,"\
        "date_start date NOT NULL," \
        "date_end date NOT NULL," \
        "date_stop date NOT NULL," \
        "date_continue date NOT NULL," \
        "PRIMARY KEY (id)" \
        ") " \
        "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return

def create_table_task():

    connect, current_connect = db_connect()

    sql = "CREATE TABLE task (" \
          "ID int(11) NOT NULL AUTO_INCREMENT," \
          "task_category varchar(30) NOT NULL," \
          "task_name varchar(255) NOT NULL," \
          "task_flag varchar(255) NOT NULL," \
          "task_description varchar(2048) NOT NULL," \
          "task_point int(4) NOT NULL," \
          "task_hint varchar(1024) NOT NULL," \
          "task_solve varchar(1024) NOT NULL," \
          "task_link varchar(512) NOT NULL," \
          "PRIMARY KEY (id)" \
          ") " \
          "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return

create_table_user()
create_table_event()
create_table_task()
