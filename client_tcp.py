import json

import requests
from Test.registration import registration_user_data
from Test.login import login_user

"""
sock = [0]*100000

for i in range(100000):
    sock[i] = socket.socket()
    sock[i].connect(('localhost', 7778))
    r = random.randint(1, 2)
    if r == 1:
        data = registration_user_data()
    else:
        data = login_user()
    print(data)
    sock[i].send(str(data).encode())

    data = sock[i].recv(2048)

    print(i, ' -> ', json.loads(data.decode()))

    sock[i].close()
"""
URL = "http://127.0.0.1:13451"
data = json.dumps({
            'Login': 'anton2',
            'Password': '2',
            'Name': '3',
            'Surname': '4',
            'Email': 'a@a.ru',
            'Sex': '5',
            'City': '6',
            'Educational': '7',
            'Logo_name': '8',
            'Logo': '9'
        })
data = requests.request('POST', '%s/registration' % URL, data={'Data': data})
print(data.text)