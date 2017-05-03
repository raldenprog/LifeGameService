# coding: utf-8
from app import app
from flask import render_template, flash, redirect, session, url_for, request
from app.forms import LoginForm, RegForm, CreateForm
from werkzeug.utils import secure_filename
import os
import sqlite3

curdir=os.path.abspath(os.curdir)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    '''тут будут таски, пока просто приветсвие пользователя'''
    if session['login']:
        login=session['login']
    return render_template('tasks.html',
                           login = login,
                           )

def getdb(table):
    '''функция получения данных из базы, передаем ей название таблицы'''
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM ' + table)
    return (cur.fetchall())
    con.close()

def createuserdb(login, email, password):
    '''функция создания пользователя
       передаем ей логин mail и pass'''
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    purchases = [(login, email, password),
                 ]
    cur.executemany('INSERT INTO users VALUES (NULL,?,?,?)', purchases)
    con.commit()
    return 1
    con.close()



@app.route('/login', methods=['GET', 'POST']) # вход пользователей
def login():
    '''вход пользователей
    сейчас тут 3 поля Login, email, password
    проверяется на правильность введенных данных через функцию getdb
    запоминаем в сессию
    '''
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Login="' + form.Login.data + '", remember_me=' + str(form.remember_me.data))
        check_pass=0
        check_user=0
        for u in getdb('users'):
            if form.Login.data==u[1]:
                check_user=1
                if form.Password.data==u[3]:
                    check_pass=1
                else:
                    return ("Wrong password")
        if check_user==0:
            return ("No such user")
        if check_user==1 and check_pass==1:
            session['login'] = form.Login.data
            return redirect(url_for('index'))
    return render_template('login.html',
                            title = 'Sign In',
                           form = form
                          )

@app.route('/logout')
def logout():
    '''функция для выхода из системы
    жмем на ссылку, нас отправляет на страницу login'''
    login=session['login']
    session.pop('login', None)
    return redirect(url_for('login'))

@app.route('/reg', methods=['GET', 'POST']) #регистрация
def reg():
    '''регистрация пользователей
    проверка на наличие пользователя через функцию getdb,
    а создание пользователя через createuserdb'''
    form = RegForm()
    if form.validate_on_submit():
        flash('Login requested for Login="' + form.Login.data)
        for u in getdb('users'):
            if form.Login.data==u[1]:
                return ("A user with this address already exists")
        createuserdb(str(form.Login.data), str(form.Email.data), str(form.Password.data))
        return redirect('/index')
    return render_template('reg.html',
                           title='Sign In',
                           form=form
                          )


@app.route('/create_task', methods=['GET', 'POST']) # функция создания таска и загрузки его
def create():
    '''создание таска 2 поля название таска, описание, и возможность загрузить файл
    создается попка uploads, в ней папка с названием таска, в ней файл с описанием и файлом'''
    check_uploads=0
    for i in os.listdir(curdir+"/"):
        if i == "uploads":
            check_uploads = 1
    if check_uploads == 0:
        os.mkdir(curdir + "/uploads/")

    form = CreateForm()
    check_folder = 0
    if request.method == 'POST':
        for i in os.listdir(curdir+"/uploads/"):
            # время ебучих костылей, потому что я не понял, как это адекватно написать пока
            # суть в том, что когда страница загружается, тут же создается папка с именем взятой из формы с названием таска, изначально форма пустая, создается папка None
            # я не знаю, как сделать, чтобы папка создавалась только после нажатия кнопки.
            #а функция os.mkdir(curdir+"/uploads/" + str(form.Name.data)) падает с ошибкой, если есть такая папка уже
            # и по этому я придумал такую хрень, проверяем есть ли у нас такая папка
            if i == "None":
                os.rmdir(curdir+"/uploads/None")
        for i in os.listdir(curdir+"/uploads/"):
            if i==form.Name.data:
                check_folder=1
        if check_folder==0:
            os.mkdir(curdir+"/uploads/" + str(form.Name.data))
            for i in os.listdir(curdir+"/uploads/"):
                if i == form.Name.data:
                    check_folder=1
        file = request.files['file']
        if file and check_folder==1:
            filename = secure_filename(file.filename)
            file.save(os.path.join(curdir+"/uploads/"+str(form.Name.data), filename))
            namefolder = curdir+"/uploads/" + str(form.Name.data) + '/'
            f = open(namefolder + 'Description for ' + str(form.Name.data), 'w')
            f.write(str(form.Text.data))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return render_template('create.html',
                           form=form
                          )


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    '''функция по идее показывает загруженный файл, сейчас заглушка'''
    return ("file was uploaded")

@app.route('/adminpanel', methods=['GET', 'POST'])
def adminpanel():
    '''панель админа создание, изменение, удаления таска'''
    return render_template('adminpanel.html')

@app.route('/remove_task', methods=['GET', 'POST'])
def remove_task():
    '''удаление таска, пока ничего'''
    return render_template('remove_task.html')
