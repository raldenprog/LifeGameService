import logging
from app.api.database.connect_db import db_connect


logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def registration_event(user_data):
    pass


def update_event(user_data):
    pass


def delete_event(user_data):
    pass


def open_event(user_data):
    pass


def close_event(user_data):
    pass