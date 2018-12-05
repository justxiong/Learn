#!/usr/bin/env python
# coding=utf-8
import socket
import time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
#s.connect(('127.0.0.1', 6666))
s.connect(('127.0.0.1', 8888))
# 接收欢迎消息:
i=0
#print(s.recv(1024).decode('utf-8'))
#for data in [b'Michael', b'Tracy', b'Sarah']:

#网络传输使用字节流格式

#数字转为字节流传输
def num2bytes():
    #'>I',>表示大端，网络序，I/H是4/2字节无符号整数
    global i
    b=struct.pack('>I',i)
    s.send(b)
    i=i+1
    time.sleep(3)

#字符串转为字节流传输
def str2bytes():
    global i
    string=bytes(str(i),'utf-8')
    #str=str(i).encode('utf-8')
    s.send(string)
    i=i+1
    time.sleep(2)

while True:
   # num2bytes()
    str2bytes()
    if i==5:
        break;
s.close()
