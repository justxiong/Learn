#!/usr/bin/env python
# coding=utf-8
import socket
import threading
import struct

#sock_dgram是udp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('127.0.0.2', 8888))
s.bind(('127.0.0.1', 8888))
#最大等待处理的连接，其后客户端连接请求将被拒绝
s.listen(5)

def recvnum(sock,addr):
    while True:
        data = sock.recv(1024)
        n=struct.unpack('>I',data)
        print("recv data is %d \n"%n)
    sock.close()

def recvstr(sock,addr):
    while True:
        try:
            data = sock.recv(1024)  #缓冲区为空将阻塞，每次send/sendall(msg)都会调用，len(msg)<n也会返回，n<len(msg)则会多次调用接收
            if not data:
                print("client disconnect!!!!!!!")
                break
            print("recv data is %s \n"%data.decode('utf-8'))
        except:
            break
    sock.close()

while True:
    # 接受一个连接:监听队列为空将阻塞,sock客户对象,addr客户ip地址
    sock, addr = s.accept()
    print('Accept new connection from %s:%s...' % addr)

    # 创建新线程来处理TCP连接:
    #t = threading.Thread(target=recvnum, args=(sock, addr))
    t = threading.Thread(target=recvstr, args=(sock, addr))
    t.start()
