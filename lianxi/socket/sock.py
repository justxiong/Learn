#!/usr/bin/env python
# coding=utf-8

import socket
from socket import getaddrinfo


info=getaddrinfo('baidu.com','www',0,socket.SOCK_STREAM,0,socket.AI_ADDRCONFIG|socket.AI_V4MAPPED)
#得到一个通过tcp连接到baidu.com主机www端口的所有可用方式

