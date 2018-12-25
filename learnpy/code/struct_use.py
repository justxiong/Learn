#!/usr/bin/env python
# coding=utf-8

import struct

'''
struct 用于处理将字节数，可用于tcp/udp中数据中数据发送接收处理，在网络编程中也有应用
如32位无符号整数，n=10240099,转变成字节，则需要依次按8位提取，struct则提供了方便的接口
struct.pack('>I',n) '>'表示大端，网络顺序，高位在低地址，H可表示2字节无符号整数
即将一个整数变为二进制，然后按8位的依次转换为十六进制

有些应用场景中如ip用一个32位整数表示，此时转换为点分十进制可用如下程序
'''
ip=3232286613
import socket
ip1=struct.pack('I',socket.htonl(ip))
#主机中数据一般是小端，htonl将其转换为网络的大端数据,pack再将其转换为字节数据
result_ip=socket.inet_ntoa(ip1)
#inet_ntoa将字节数据转换为点分十进制数据
print(result_ip)

#gdb直接看p /x ip 得到十六进制数据,再一个个字节转换
