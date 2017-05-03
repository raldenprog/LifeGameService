# coding: utf-8
from flask_wtf import Form
from wtforms import TextField, BooleanField, StringField, validators
from wtforms.validators import Required


class LoginForm(Form):
    Login = TextField('Login', validators=[Required()])
    Password = TextField('Password', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)


class RegForm(Form):
    Login = TextField('Login', validators=[Required()])
    Password = TextField('Password', validators=[Required()])
    Email = TextField('Password', validators=[Required()])


class CreateForm(Form):
    Name = StringField('Name', validators=[Required()])
    Text = TextField('Text', validators=[Required()])
    Flag = TextField('Flag', validators=[Required()])
