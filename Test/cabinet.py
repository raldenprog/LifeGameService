from app.api.user_cabinet.cabinet import user_cabinet


def cabinet_done():
    data = {
        "id": "1"
    }
    print(user_cabinet(data))


def cabinet_error():
    data = {
        'login': 'Anton'
    }
    print(user_cabinet(data))


cabinet_done()
cabinet_error()
