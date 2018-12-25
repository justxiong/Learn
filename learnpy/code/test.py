#!/usr/bin/env python
#coding=utf-8


import copy

D1 = {'user': 'runoob', 'num': [1, 2, 3]} # 原始数据
D2 = D1  # 直接引用：D2和D1整体指向同一对象。
D3 = D1.copy()  # 浅拷贝：D3和D1的父对象是一个独立的对象，但是他们的子对象还是指向同一对象。
D4 = copy.deepcopy(D1)  # 深拷贝：D4和D1的整体是一个独立的对象。

D1['user'] = 'root' # 修改父对象D1
D1['num'].remove(1) # 修改父对象D1中的[1, 2, 3]列表子对象

print('原始数据:',{'user': 'runoob', 'num': [1, 2, 3]}) # 原始数据
print('改后数据:',D1) # 父子都修改过的
print('直接引用:',D2) # 父子都变(直接引用)
print('浅拷贝:',D3) # 父不变，子变(浅拷贝)
print('深拷贝:',D4) # 父子都不变(深拷贝)
