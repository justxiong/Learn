#!/usr/bin/env python
# coding=utf-8

#user_obj_info={'name':'xongjian','passwd':'123456','mon':3000,'shoplist':[[('mac',20000),2],[('phone',10000),1]]}

import os
goods = [(1,{"name": "电脑", "price": 1999}),(2,{"name": "鼠标", "price": 10}),(3,{"name": "游艇", "price": 20}),
(4,{"name": "美女", "price": 998})]

username=input('请输入账号:')
password=input('请输入密码:')
isNewUser=True

def print_user_info():
    print('Hello {u_name},you have buy:{item} and you have left {salary}'.format(u_name=user_obj['name'],item=user_obj['shoplist'],salary=user_obj['mon']))

with open('userinfo.txt','r') as user_file:
    for i in user_file.readlines():
        if i[0]=='\n':
            break;
        user_obj=eval(i)
        #print(user_obj)
        #非json格式，采用eval得到字符串中表达式即dict对象
        if username==user_obj['name']:
            if password==user_obj['passwd']:
                isNewUser=False
                print_user_info()
                break
            else:
                while True:
                    password=input('密码错误，请重新输入,q退出:')
                    if password=='q':
                        exit()
                    elif password==user_obj['passwd']:
                        isNewUser=False
                        print_user_info()
                    else:
                        continue
        else:
            continue

with open('userinfo.txt','a') as user_file:
    if isNewUser:
        salary=input('欢迎首次登陆，请输入您的工资:')
        if salary=='q':
            exit()
        user_obj={}
        user_obj['name']=username
        user_obj['passwd']=password
        user_obj['mon']=int(salary)
        user_obj['shoplist']=[]
        user_file.write(str(user_obj)+'\n')

    print('可购买商品有 {items}: \n'.format(items=goods))
    print('选择编号购买或q退出')
    while True:
        selected=input('选择编号:')
        if selected =='q':
            break
        elif selected.isdigit():
            selected=int(selected)-1
            if user_obj['mon']>=goods[selected][1]['price']:
                items=[]
                items.append(goods[selected][1]['name'])
                items.append(goods[selected][1]['price'])
                item=tuple(items)
                print('change is {it}'.format(it=item))
                print('buy is {buy}'.format(buy=user_obj['shoplist']))
                if not user_obj['shoplist']:
                    user_obj['shoplist'].append([item,1])
                else:
                    for n,i in enumerate(user_obj['shoplist']):
                        if item == i[0]:
                            user_obj['shoplist'][n][1]=user_obj['shoplist'][n][1]+1
                            item=[]
                            break
                    if item:
                        user_obj['shoplist'].append([item,1])
                user_obj['mon']=user_obj['mon']-goods[selected][1]['price']
                print('you have buy:{item} and you have left {salary}'.format(item=user_obj['shoplist'],salary=user_obj['mon']))
            else:
                print('your money not enough')
        else:
            print('输入格式不正确')

#文本内容替换先读入所有行，再修改匹配行，并依次写入

#用户已被写入，但购物信息需要更新
with open('userinfo.txt','r') as user_file:
    lines=user_file.readlines()

with open('userinfo.txt','w') as user_file:
        userObjWrited=False

        for line in lines:
            obj=eval(line)
            if obj['name']==user_obj['name']:
                line=(str(user_obj)+'\n')
                userObjWrited=True
            user_file.write(line)


#对于for i in list/tuple/dict等 i 取得的是序列中元素的拷贝值，无法直接修改序列元素值，需要通过下标/键来访问序列才能修改
