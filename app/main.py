import asyncio
import logging
import socket
import json
import threading
from app.api.database.registration_users import add_user
from app.api.database.login_user import login_verification


logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


def func1(data, writer):
    print('func1 -> ', data)
    data = login_verification(data)
    print(data)
    data = json.dumps(data)
    writer.send(data.encode())
    writer.close()


def func2(data, writer):
    print('func2 -> ', data)
    data = add_user(data)
    print(data)
    data = json.dumps(data)
    writer.send(data.encode())
    writer.close()
"""
async def main_server(reader, writer):
    print('Connection from {}'.format(
       writer.get_extra_info('peername')
    ))
    data = await reader.read(2048)
    data = data.decode()
    data = json.loads(data)
    print('Action = ', data['Action'])
    if data['Action'] == 'Login':
        thread = threading.Thread(target=func1, args=(data['data'], writer))
    elif data['Action'] == 'Registration':
        thread = threading.Thread(target=func2, args=(data['data'], writer))
    else:
        ans = "Error"
    thread.start()
"""


def quest(data, conn):
    print('Action = ', data['Action'])
    if data['Action'] == 'Add_user':
        thread = threading.Thread(target=func1, args=(data['Data'], conn))
    elif data['Action'] == 'Registration_user':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Update_event':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Scoreboard_all_user':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Scoreboard_event_users':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_create_one_task':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_create_few_tasks':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_get_task_event_name':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Task_get_task_event_category':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'User_cabinet':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Change_password':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    elif data['Action'] == 'Edit_cabinet':
        thread = threading.Thread(target=func2, args=(data['Data'], conn))
    else:
        ans = {"Error": "Action error"}
    thread.start()


if __name__ == "__main__":
    sock = socket.socket()
    try:
        sock.bind(("127.0.0.1", 7777))
        sock.listen(10)
        while True:
            conn, addr = sock.accept()
            data = conn.recv(2048)
            data = data.decode()
            data = json.loads(data)
            quest(data, conn)
    finally:
        sock.close()
    print()
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.ensure_future(
            asyncio.start_server(main_server, '127.0.0.1', 7777),
            loop=loop
        )
    )
    loop.run_forever()
    """