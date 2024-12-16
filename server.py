from socket import *
from time import ctime

HOST = ' '
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpserSock = socket(AF_INET,SOCK_STREAM)
tcpserSock.bind(ADDR)
tcpserSock.listen(5)
while True:
    print("waiting for connection")
    tcpcliSock,addr = tcpserSock.accept()
    print("connected from: ",addr)
    while True:
        data = tcpcliSock.recv(BUFSIZ)
        if not data:
            break
        tcpcliSock.send('[%s] %s' % (ctime(),data))
    tcpcliSock.close()
tcpserSock.close()

