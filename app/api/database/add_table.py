# coding=utf-8
import sys
import os
print(os.getcwd())
sys.path.append(os.getcwd()+'/../../')
from api.database.connect_db import db_connect_new as db_connect
from api.auth.registration_users import registration_user

def create_table_user():
    connect, current_connect = db_connect()
    sql = """--drop table users;


CREATE TABLE public.users
(
    id_user SERIAL NOT NULL,
    name text COLLATE pg_catalog."default",
    surname text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    sex text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    educational text COLLATE pg_catalog."default",
    logo text COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY (id_user)
)"""
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_auth():
    connect, current_connect = db_connect()
    sql = """CREATE TABLE auth
(
    id_user SERIAL NOT NULL,
    login text COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_pkey PRIMARY KEY (id_user),
    CONSTRAINT auth_login_key UNIQUE (login)
) """
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_access():
    connect, current_connect = db_connect()
    sql = """--DROP TABLE access;

CREATE TABLE access
(
    id_user integer NOT NULL,
    access integer NOT NULL DEFAULT 0,
    CONSTRAINT access_pkey PRIMARY KEY (id_user)
) """
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_session():
    connect, current_connect = db_connect()
    sql = """CREATE TABLE Session (
          Session SERIAL NOT NULL,
          id_user integer NOT NULL,
          UUID char(256) NOT NULL UNIQUE,
          PRIMARY KEY (Session)
          ) """
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_event():
    connect, current_connect = db_connect()
    sql = """-- Table: public.event

DROP TABLE event;

CREATE TABLE event
(
    id_event SERIAL NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    logo text COLLATE pg_catalog."default" NOT NULL,
    date_start timestamp(6) without time zone NOT NULL,
    date_end timestamp(6) without time zone NOT NULL,
    date_stop timestamp(6) without time zone NOT NULL,
    date_continue timestamp(6) without time zone NOT NULL,
    status integer,
    CONSTRAINT event_pkey PRIMARY KEY (id_event)
)


-- DROP INDEX public.event_id_event_close;

CREATE INDEX event_id_event_close
    ON event USING btree
    (id_event DESC, status)
    TABLESPACE pg_default    
    WHERE status = 1
;"""
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_task():

    connect, current_connect = db_connect()

    sql = """CREATE TABLE task (
          id_task SERIAL NOT NULL,
          Task_category varchar(30) NOT NULL,
          Task_name varchar(255) NOT NULL UNIQUE,
          Task_flag varchar(255) NOT NULL,
          Task_description varchar(2048) NOT NULL,
          Task_point integer NOT NULL,
          Task_hint varchar(1024) NOT NULL,
          Task_solve varchar(1024),
          Task_link varchar(512),
          Status integer,
          Public_status integer,
          id_event integer,
          PRIMARY KEY (id_task)
          )"""
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return


def create_table_task_acc():

    connect, current_connect = db_connect()

    sql = """CREATE TABLE task_acc (
          id SERIAL NOT NULL,
          id_task integer NOT NULL,
          id_user integer NOT NULL,
          point integer NOT NULL,
          UNIQUE(id_task, id_user),
          PRIMARY KEY (id)
          );"""
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return

def create_table_news():

    connect, current_connect = db_connect()

    sql = """CREATE TABLE news (
              id_news SERIAL NOT NULL,
              News_text text NOT NULL,
              id_user integer NOT NULL,
              Likes_count integer NOT NULL,
              Dislikes_count integer NOT NULL,
              Data timestamp NOT NULL,
              PRIMARY KEY (id_news)
              );"""
    print(sql)
    try:
        current_connect.execute(sql)
        current_connect.close()
    except:
        return

def create_table_comments():

    connect, current_connect = db_connect()

    sql = """CREATE TABLE comments (
              id_comment SERIAL NOT NULL,
              id_news integer NOT NULL,
              id_comment_parent integer NOT NULL,
              Comment_text text NOT NULL,
              id_user integer NOT NULL,
              Likes_count integer NOT NULL,
              Dislikes_count integer NOT NULL,
              Data timestamp NOT NULL,
              PRIMARY KEY (id_comment)
              );"""
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
    check = [names.LOGIN, names.PASSWORD, names.NAME,
             names.SURNAME, names.EMAIL, names.SEX,
             names.CITY, names.EDUCATION, names.LOGO_NAME, names.LOGO]
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
        registration_data[names.LOGIN] = d[i]
        registration_data[names.PASSWORD] = password[i]
        registration_user(registration_data)

create_table_auth()
create_table_user()
create_table_access()
create_table_session()
# SCTF()
create_table_event()
create_table_task()
create_table_task_acc()
#create_users()

