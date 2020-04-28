#!/usr/bin/env python3.6
# coding=utf-8
import hashlib
import uuid
from api.service import GameService as gs


class Registration:
    """
    Класс регистрации
    """

    @staticmethod
    def input_auth_table(login, password):
        """
        Заносится изменение в таблицу auth
        """
        password_hash = hashlib.md5()
        password_hash.update(password.encode())
        password = password_hash.hexdigest()
        sql = f"""INSERT INTO Auth (login, password) VALUES ('{login}', '{password}') RETURNING id_user"""
        id_user = gs.SqlQuery(sql)[0]['id_user']
        return id_user

    @staticmethod
    def input_access_table(id_user):
        """
        Метод заносит данные в таблицу "Права доступа"
        """
        sql = f"""INSERT INTO Access VALUES ({id_user} ,0)"""
        gs.SqlQuery(sql)

    @staticmethod
    def input_user_table(id_user, name, email):
        """
        Метод добавляет данные в таблицу "Информация о пользователе"
        """
        sql = f"""INSERT INTO Users VALUES ({id_user}, '{name}', '{email}')"""
        gs.SqlQuery(sql)

    @staticmethod
    def input_session_table(id_user):
        """
        Метод регистрирует данные в таблицы "Сессии пользователей"
        """
        uuid_user = str(uuid.uuid4())
        sql = f"""INSERT INTO Session (id_user, uuid) VALUES ({id_user}, '{uuid_user}')"""
        gs.SqlQuery(sql)
        return uuid_user

    def registration_user(self, login, password, name, email):
        """
        Метод проверяет корректность введенных данных
        """
        id_user = self.input_auth_table(login, password)
        self.input_access_table(id_user)
        self.input_user_table(id_user, name, email)
        uuid_user = self.input_session_table(id_user)
        return uuid_user
