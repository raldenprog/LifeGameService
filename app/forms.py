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
    Name = TextField('Name', validators=[Required()])
    Patronymic = TextField('Patronymic', validators=[Required()])
    Email = TextField('Email', validators=[Required()])
    Sex = TextField('Sex', validators=[Required()])
    City = TextField('City', validators=[Required()])
    Educational = TextField('Educational', validators=[Required()])
    Logo = TextField('Logo', validators=[Required()])


class CreateForm(Form):
    Name = StringField('Name', validators=[Required()])
    Text = TextField('Text', validators=[Required()])
    Flag = TextField('Flag', validators=[Required()])
