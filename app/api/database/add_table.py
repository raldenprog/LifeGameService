import pymysql
from app.api.database.connect_db import db_connect


def create_table_user():
    connect, current_connect = db_connect()
    sql = "CREATE TABLE Users (" \
        "@User int(11) AUTO_INCREMENT," \
        "Name varchar(32)," \
        "Surname varchar(32),"\
        "Email varchar(64)," \
        "Sex varchar(6)," \
        "City varchar(64)," \
        "Educational varchar(255)," \
        "Logo varchar(256)," \
        "PRIMARY KEY (@User)" \
        "foreign key (@User) references Auth (@User)," \
        "on delete cascade" \
        "on update cascade" \
        ") " \
        "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_login():
    connect, current_connect = db_connect()
    sql = "CREATE TABLE Auth (" \
        "@User int(11) auto_increment," \
        "Login varchar(30) NOT NULL UNIQUE," \
        "Password varchar(40) NOT NULL," \
        "PRIMARY KEY (@User)" \
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
          "@User int(11) NOT NULL AUTO_INCREMENT," \
          "Access int(1) NOT NULL," \
          "PRIMARY KEY (@User)," \
          "foreign key (@User) references Auth (@User)," \
          "on delete cascade" \
          "on update cascade" \
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
          "@Session int(11) NOT NULL AUTO_INCREMENT," \
          "@User int(11) NOT NULL," \
          "GUID varchar(256) NOT NULL UNIQUE," \
          "PRIMARY KEY (@Session)," \
          "foreign key (@User) references Auth (@User)," \
          "on delete cascade" \
          "on update cascade" \
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
          "status int(1) NOT NULL" \
          "public_status int(1) NOT NULL" \
          "event varchar(255) NOT NULL" \
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
