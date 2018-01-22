__author__ = 'ar.chusovitin'

from api.service import GameService as gs
import api.database.connect_db as cd


def Query(sql):
    connect, current_connect = cd.db_connect()
    print(connect)
    current_connect.execute(sql)
    result = current_connect.fetchall()
    return result


def auth():
    sql = """select * from Auth"""
    result = Query(sql)
    for i in result:
        sql = '''INSERT INTO auth(id_user, login, password)
        VALUES ({id_user},\'{login}\',\'{password}\')'''.format(id_user=i['User'], login=i[names.LOGIN], password=i[names.PASSWORD])
        print(sql)
        gs.SqlQuery(sql)


def auth():
    sql = """select * from Access"""
    result = Query(sql)
    for i in result:
        sql = '''INSERT INTO access
        VALUES ({id_user},{access})'''.format(id_user=i['User'], access=i['Access'])
        print(sql)
        gs.SqlQuery(sql)


def Event():
    sql = """select * from Event"""
    result = Query(sql)
    for i in result:
        sql = '''INSERT INTO event
        VALUES ({id_event},'{name}','{description}','1','1',now(),now(),now(),now())'''.format(id_event=i['Event'], name=i[names.NAME], description=i['Description'])
        print(sql)
        gs.SqlQuery(sql)


def session():
    sql = """select * from Session"""
    result = Query(sql)
    for i in result:
        sql = '''INSERT INTO session
        VALUES ({session},'{id_user}','{uuid}')'''.format(session=i['Session'], id_user=i['User'], uuid=i['UUID'])
        print(sql)
        gs.SqlQuery(sql)



def task():
    sql = """select * from task"""
    result = Query(sql)
    for i in result:
        sql = '''INSERT INTO task
        VALUES ({ID_Task},'{Task_category}','{Task_name}','{Task_flag}',
        '{Task_description}','{Task_point}','{Task_hint}','{Task_solve}','{Task_link}',{Status}, {Public_status}, {id_Event})'''.format(**i)
        print(sql)
        gs.SqlQuery(sql)


def task_acc():
    sql = """select * from task_acc"""
    result = Query(sql)
    for i in result:
        sql = '''INSERT INTO task_acc
        VALUES ({id},{id_task},{id_user},{id_event},
        {point},'{time}')'''.format(**i)
        print(sql)
        gs.SqlQuery(sql)

def user():
    sql = """select * from Users"""
    result = Query(sql)
    for i in result:
        print(i)
        sql = '''INSERT INTO users
        VALUES ({User},'{Name}','{Surname}','{Email}',
        '{Sex}','{City}','{Educational}','{Logo}')'''.format(**i)
        print(sql)
        gs.SqlQuery(sql)
user()