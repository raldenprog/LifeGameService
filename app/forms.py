# coding: utf-8
from flask_wtf import Form
from wtforms import TextField, BooleanField, StringField, validators, FileField, SelectField
from wtforms.validators import Required
import re

class LoginForm(Form):
    Login = StringField('Login', [validators.required()])
    Password = StringField('Password', [validators.required()])
    remember_me = BooleanField('remember_me', default=False)


class RegForm(Form):
    Login = StringField('Login', [validators.required()])
    Password = StringField('Password', [validators.required()])
    Name = StringField('Name', [validators.required()])
    Patronymic = StringField('Patronymic', [validators.required()])
    Email = StringField('Email', [validators.email(), validators.required()])
    Sex = SelectField('Sex', choices=[('male', 'male'), ('female', 'female')])
    City = StringField('City', [validators.required()])
    Educational = StringField('Educational', [validators.required()])
    Logo = FileField('Logo')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class CreateForm(Form):
    Name = StringField('Name', [validators.required()])
    Text = StringField('Text', [validators.required()])
    Flag = StringField('Flag', [validators.required()])
