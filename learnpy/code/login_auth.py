#!/usr/bin/env python
# coding=utf-8

import os

vip_username = {'james':123456,'wade':234567,'park':345678,'harden':456789}
#vip_password = ['123456','234567','345678','456789']
count = 0

while True:
    username=input('请输入用户名:').strip()
    if username not in vip_username:
        print('用户名不存在')
        continue
    else:
        #'r+'读写
        #if not os.path.exists('/tmp/userstate.txt'):
        #    open('/tmp/userstate.txt','w+') as userstate: 文件不存在则创建一个用于读写文件，存在则会删除原内容从头开始读写，为避免覆盖最好在检测中使用
        try:
            with open('/tmp/userstate.txt','r+') as userstate:
                name_list = userstate.read()
                if username in name_list:
                    print('user has locked')
                    break;
        except FileNotFoundError as e:
            os.mknod('/tmp/userstate.txt')#only linux
    while True:
        passwd=input('请输入密码:').strip()
        if vip_username[username] == int(passwd):
            count=0
            print('Congratulation {user} login success'.format(user=username))
            break
        else:
            print('password error')
            count=count+1
            if count==3:
                #'a'追加
                with open('/tmp/userstate.txt','a') as userstate:
                    userstate.write(username)
                    print('User {un} has been locked'.format(un=username))
                    break

