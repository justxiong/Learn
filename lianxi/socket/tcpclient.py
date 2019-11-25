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

#tcp 拆包重组
    #tcp中数据流可能发生拆包重组如发送缓冲区不够，tcp会自行将流分为多个数据包，分别发送然后在接收端重组，udp则会发送完整数据报，只有成功发送和失败两种状态.因此tcp中需要在发送和接收时考虑数据包的完整性问题
      #对发送而言send调用可能发生拆包现象(部分传输)，需要用户通过返回值判断，返回值就是实际发送的字节数，因此需要在一个循环内调用send直到所有数据全部发送(上面程序不够严谨)。对于这个python标准库中提供了友好的sendall()接口该函数由c实现且内部封装了循环，因此可以确保数据完整发送.
#对接收而言recv也需要考虑完整性问题，但这个没有好的标准实现.由于无法预测要接受的数据长度，recv总需要放在循环中，直到合适条件跳出.send/sendall(msg),recv(n) 每次发送都会recv,如果n<len(msg)则一次send有多次recv,n>len也会返回一次
#send/recv数据都是发送或接收自系统的tcp栈缓冲区,缓冲区大小由系统决定，一旦满后tcp的拥塞控制会停止发送或接收send/recv阻塞
#sock.shutdown(socket.SHUT_WR) 将通信连接半关闭，此时套接字不会关闭，调用方不再写数据，接收方的recv会收到空字符.RD表示调用方不再接收，如果对方继续发送会报错。socket是双向的，shutdown可以定向关闭socket

    #模式一:发送方使用sendall,发送完后调用close.接收方循环中调用recv,直达接收到空字符(即发送方调用了close)，这种方式常用于一些简单的网络协议.
    #模式二:在模式一下调用shutdown,是接收方收到空字符
    #模式3:使用定长消息，用于一些特定应用
    #模式4:使用特定符号作为结束的定界符，如果消息使用字符有限还可以否则需要转义，处理会比较麻烦
    #模式5:在每个消息前面加上其长度作为前缀，接后方解码长度在进入循环常用于一些高性能协议
    #模式6:在不知道流长度下，可以将流拆为多个数据块分块发送然后和５类似
    #也可以混合使用，如http就是混合45


    #公钥　证书　tls,ssl,openssl流程与关系
