# coding: utf-8
from app import app

from app.database import get_user, registration_users
from flask import render_template, flash, redirect, session, url_for, request
from app.forms import LoginForm, RegForm, CreateForm
from werkzeug.utils import secure_filename
import os
import sqlite3


@app.after_request
def patch_response(response):
    response.headers['Content-Security-Policy'] = \
        "default-src 'self' 'unsafe-inline';"
    return response


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    """тут будут таски, пока просто приветсвие пользователя
    """
    user_login = None
    if session["login"]:
        user_login = session["login"]
    return render_template("tasks.html", login=user_login)




@app.route('/login', methods=['GET', 'POST'])       # вход пользователей
def login():
    """вход пользователей
    сейчас тут 3 поля Login, email, password
    проверяется на правильность введенных данных через функцию get_table
    запоминаем в сессию
    """
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for Login=\"" + form.Login.data + "\", remember_me=" + str(form.remember_me.data))
        check_pass = 0
        check_user = 0
        users = get_user.get_table("users")
        # Оставляю пока так, позже нужно переписать
        if users is not None:
            for user in users:
                if form.Login.data == user[1]:
                    check_user = 1
                    if form.Password.data == user[3]:
                        check_pass = 1
                    else:
                        return "Wrong password"
            if check_user == 0:
                return "No such user"
            if check_user == 1 and check_pass == 1:
                session['login'] = form.Login.data
                return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    """функция для выхода из системы
    жмем на ссылку, нас отправляет на страницу login
    """
    session.pop("login", None)
    return redirect(url_for('login'))


@app.route("/registration", methods=["GET", "POST"])
def reg():
    """регистрация пользователей
    проверка на наличие пользователя через функцию getdb,
    а создание пользователя через add_user
    """
    form = RegForm()
    if form.validate_on_submit():
        print(form.Login.data)
        print(get_user.get_table(form.Login.data))
        flash("Login requested for Login=\"" + form.Login.data)
        if get_user.get_table(form.Login.data) > 0:
            return "A user with this address already exists"
        else:
            registration_data = {
                'login': str(form.Login.data),
                'password': str(form.Password.data),
                'name': str(form.Name.data),
                'patronymic': str(form.Patronymic.data),
                'email': str(form.Email.data),
                'sex': str(form.Sex.data),
                'city': str(form.City.data),
                'Educational': str(form.Educational.data),
                'logo': str(form.Logo.data)
            }
            print(registration_data)
            registration_users.add_user(registration_data)
            return redirect('/')
    print("Nooooononononono")
    return render_template('reg.html', title='Sign In', form=form)


@app.route("/create_task", methods=['GET', 'POST'])
def create():
    """создание таска 2 поля название таска, описание, и возможность загрузить файл
    создается попка uploads, в ней папка с названием таска, в ней файл с описанием и файлом
    """
    current_dir = os.path.abspath(os.curdir)
    check_uploads = 0
    for i in os.listdir(current_dir + "/"):
        if i == "uploads":
            check_uploads = 1
    if check_uploads == 0:
        os.mkdir(current_dir + "/uploads/")

    form = CreateForm()
    check_folder = 0
    if request.method == 'POST':
        for i in os.listdir(current_dir + "/uploads/"):
            """ время ебучих костылей, потому что я не понял, как это адекватно написать пока
            суть в том, что когда страница загружается, тут же создается папка с именем взятой из формы
            с названием таска, изначально форма пустая, создается папка None
            я не знаю, как сделать, чтобы папка создавалась только после нажатия кнопки.
            а функция os.mkdir(curdir+"/uploads/" + str(form.Name.data)) падает с ошибкой, если есть такая папка уже
            и по этому я придумал такую хрень, проверяем есть ли у нас такая папка
            """
            if i is None:
                os.rmdir(current_dir + "/uploads/None")
        for i in os.listdir(current_dir + "/uploads/"):
            if i == form.Name.data:
                check_folder = 1
        if check_folder == 0:
            os.mkdir(current_dir + "/uploads/" + str(form.Name.data))
            for i in os.listdir(current_dir + "/uploads/"):
                if i == form.Name.data:
                    check_folder = 1
        file = request.files['file']
        if file and check_folder == 1:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_dir+"/uploads/"+str(form.Name.data), filename))
            name_folder = current_dir+"/uploads/" + str(form.Name.data) + '/'
            f = open(name_folder + 'Description for ' + str(form.Name.data), 'w')
            f.write(str(form.Text.data))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('create.html', form=form)


@app.route("/uploads/<filename>")
def uploaded_file():
    """функция по идее показывает загруженный файл, сейчас заглушка
    """
    return "file was uploaded"


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    """панель админа создание, изменение, удаления таска
    """
    return render_template('adminpanel.html')


@app.route("/remove_task", methods=['GET', 'POST'])
def remove_task():
    """удаление таска, пока ничего
    """
    return render_template('remove_task.html')
