# coding: utf-8
from flask_wtf import Form
from wtforms import BooleanField, StringField, validators, FileField, SelectField


class LoginForm(Form):
    Login = StringField('Login', [validators.required()])
    Password = StringField('Password', [validators.required()])
    remember_me = BooleanField('remember_me', default=False)


class RegForm(Form):
    Login = StringField('Login', [validators.required()])
    Password = StringField('Password', [validators.required()])
    Repeat_password = StringField('Repeat_password', [validators.required()])
    Name = StringField('Name', [validators.required()])
    Patronymic = StringField('Patronymic', [validators.required()])
    Email = StringField('Email', [validators.email(), validators.required()])
    Sex = SelectField('Sex', choices=[('male', 'male'), ('female', 'female')])
    City = StringField('City', [validators.required()])
    Educational = StringField('Educational', [validators.required()])
    Logo = FileField('Logo')


class CreateForm(Form):
    Name = StringField('Name', [validators.required()])
    Text = StringField('Text', [validators.required()])
    Flag = StringField('Flag', [validators.required()])
