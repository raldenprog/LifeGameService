import socket
import random
import json
from Test.registration import registration_user_data
from Test.login import login_user


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


