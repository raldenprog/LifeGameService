# coding=utf-8
import sys
import os
print(os.getcwd())
sys.path.append(os.getcwd()+'/../../')
from api.database.connect_db import db_connect
from api.auth.registration_users import registration_user

def create_table_user():
    connect, current_connect = db_connect()
    sql = "CREATE TABLE Users (" \
        "User int(11) AUTO_INCREMENT, " \
        "Name varchar(32), " \
        "Surname varchar(32), "\
        "Email varchar(64), " \
        "Sex varchar(8), " \
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
        "Logo varchar(30) NOT NULL, " \
        "Status varchar(30) NOT NULL, "\
        "Date_start date NOT NULL, " \
        "Date_end date NOT NULL, " \
        "Date_stop date NOT NULL, " \
        "Date_continue date NOT NULL, " \
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
          "ID_Task int(11) NOT NULL AUTO_INCREMENT, " \
          "Task_category varchar(30) NOT NULL, " \
          "Task_name varchar(255) NOT NULL UNIQUE, " \
          "Task_flag varchar(255) NOT NULL, " \
          "Task_description varchar(2048) NOT NULL, " \
          "Task_point int(4) NOT NULL, " \
          "Task_hint varchar(1024) NOT NULL," \
          "Task_solve varchar(1024), " \
          "Task_link varchar(512), " \
          "Status int(1), " \
          "Public_status int(1), " \
          "id_Event int(11), " \
          "PRIMARY KEY (ID_Task)" \
          ") " \
          "ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_task_acc():

    connect, current_connect = db_connect()

    sql = "CREATE TABLE task_acc (" \
          "id int(11) NOT NULL AUTO_INCREMENT, " \
          "id_task int(11) NOT NULL, " \
          "id_user int(11) NOT NULL, " \
          "point int(4) NOT NULL, " \
          "UNIQUE(id_task, id_user), " \
          "PRIMARY KEY (id)" \
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


def SCTF():
    check = ['Login', 'Password', 'Name',
             'Surname', 'Email', 'Sex',
             'City', 'Educational', 'Logo_name', 'Logo']
    d = ['Make society (h)acked again', 'Без пафоса', 'Лицей7', 'HackSQUAD',
         'Jackzkers', 'd34dl1n3', 'rm404', 'GSV', 'Difensori',
         'ОвощиV2.0', 'Not Found', 'CLAY', 'Трисомия по хромосоме',
         'Грядка Хокинга', 'FoXXeS', 'Колбаса по рубль двадцать']
    password = ['ozpbjhhssc', 'xorbpconpb', 'bbcyhqphrb', 'tcpbptuyke',
                'wimgygepek', 'ffornthbxq', 'njjwpmgzpy', 'hcxleuhdxf',
                'zsednvqteg', 'ldsyaprlrs', 'lantvvwsrn', 'nwnutdkyow',
                'sdzjjhjfnb', 'yylopsahxa', 'advrcgfhca', 'bxjpmgcejx']

    d = ['test3']
    password = ['test3']
    registration_data = dict.fromkeys(check, '-')
    for i in range(len(d)):
        registration_data['Login'] = d[i]
        registration_data['Password'] = password[i]
        registration_user(registration_data)


#  create_table_auth()
# create_table_user()
# create_table_access()
# create_table_session()
SCTF()
# create_table_event()
# create_table_task()
# create_table_task_acc()
# create_users()
