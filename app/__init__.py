# coding: utf-8
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__, static_url_path = "", static_folder = "tmp/")

app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models
