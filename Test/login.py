from app.api.database.login_user import login_verification


def login_done():
    data = {
        'login': 'Anton',
        'password': 'qwerty'
    }
    print(login_verification(data))


def login_error():
    data = {
        # 'login': 'Anton',
        'password': 'qwerty'
    }
    print(login_verification(data))


login_done()
login_error()
