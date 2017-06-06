import socket
sock = [0]*1000
for i in range(1000):
    sock[i] = socket.socket()
    sock[i].connect(('localhost', 7777))
    sock[i].send(b'hello, world!')
    data = sock[i].recv(1024)
    print(i, ' -> ', data)

for i in range(1000):
    sock[i].close()


