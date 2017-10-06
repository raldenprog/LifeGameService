import pymysql
from app.api.database.connect_db import db_connect


def create_table_user():
    connect, current_connect = db_connect()
    sql = "CREATE TABLE Users (" \
        "User int(11) AUTO_INCREMENT, " \
        "Name varchar(32), " \
        "Surname varchar(32), "\
        "Email varchar(64), " \
        "Sex varchar(6), " \
        "City varchar(64), " \
        "Educational varchar(255), " \
        "Logo varchar(256), " \
        "PRIMARY KEY (User) " \
        ") " \
        "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_auth():
    connect, current_connect = db_connect()
    sql = "CREATE TABLE Auth (" \
        "User int(11) auto_increment," \
        "Login varchar(30) NOT NULL UNIQUE," \
        "Password varchar(40) NOT NULL," \
        "PRIMARY KEY (User)" \
        ") " \
        "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_access():
    connect, current_connect = db_connect()
    sql = "CREATE TABLE Access (" \
          "User int(11) NOT NULL AUTO_INCREMENT," \
          "Access int(1) NOT NULL DEFAULT 0," \
          "PRIMARY KEY (User)" \
          ") " \
          "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_session():
    connect, current_connect = db_connect()
    sql = "CREATE TABLE Session (" \
          "Session int(11) NOT NULL AUTO_INCREMENT," \
          "User int(11) NOT NULL," \
          "UUID varchar(256) NOT NULL UNIQUE," \
          "PRIMARY KEY (Session)" \
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
        "Event int(11) NOT NULL AUTO_INCREMENT, " \
        "Name varchar(255) NOT NULL, " \
        "Description varchar(2048) NOT NULL, " \
        "Logo varchar(256) NOT NULL, " \
        "Status varchar(30) NOT NULL, "\
        "Date_start int(11) NOT NULL, " \
        "Date_end int(11) NOT NULL, " \
        "Date_stop int(11) NOT NULL, " \
        "Date_continue int(11) NOT NULL, " \
        "PRIMARY KEY (Event)" \
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
          "Task int(11) NOT NULL AUTO_INCREMENT, " \
          "Task_category varchar(30) NOT NULL, " \
          "Task_name varchar(255) NOT NULL, " \
          "Task_flag varchar(255) NOT NULL, " \
          "Task_description varchar(2048) NOT NULL, " \
          "Task_point int(4) NOT NULL, " \
          "Task_hint varchar(1024) NOT NULL," \
          "Task_solve varchar(1024) NOT NULL, " \
          "Task_link varchar(512) NOT NULL, " \
          "Status int(1) NOT NULL, " \
          "Public_status int(1) NOT NULL, " \
          "Event varchar(255) NOT NULL, " \
          "PRIMARY KEY (Task)" \
          ") " \
          "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_users():

    sql = [
        "INSERT INTO Auth(User, Login, Password) VALUES(1, 'Anton1', 'qwerty');",
        "INSERT INTO Auth(User, Login, Password) VALUES(2, 'Anton2', 'qwerty');",
        "INSERT INTO Auth(User, Login, Password) VALUES(3, 'Anton3', 'qwerty');"
        "INSERT INTO Auth(User, Login, Password) VALUES(4, 'Anton4', 'qwerty');"
        ]
    for execute in sql:
        connect, current_connect = db_connect()
        try:
            data = current_connect.execute(execute)
        finally:
            current_connect.close()


# create_table_auth()
# create_table_user()
# create_table_access()
# create_table_session()
create_table_event()
# create_table_task()
# create_users()
