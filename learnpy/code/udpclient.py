#!/usr/bin/env python
# coding=utf-8

import socket
import struct
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
i=0
while True:
    data=struct.pack('>i',i)
    print('data is %s \n'%data)
    s.sendto(data,('127.0.0.1',8888))
    time.sleep(2)
    i=i+1
    print('i is %d\n'%i)
s.close()
