#!/usr/bin/env python
# coding=utf-8
def triangles():
    res=[1]
    n=1
    while True:
        if(n==1):
             n=n+1
             yield res[:]
        elif(n==2):
            n=n+1
            res.append(1)
            yield res[:]
        else:
            temp=res[:]
            for i in list(range(n-2)):
                res[i+1]=temp[i]+temp[i+1]
            res.append(1)
            n=n+1
            yield res[:]

def triangles1():
    res=[1]
    n=1
    while True:
        if(n==1):
             n=n+1
             yield res
        elif(n==2):
            n=n+1
            res.append(1)
            yield res
        else:
            temp=res
            for i in list(range(n-2)):
                res[i+1]=temp[i]+temp[i+1]
            res.append(1)
            n=n+1
            yield res

n = 0
results = []
for t in triangles():
#for t in triangles1():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


'''
以generator生成杨辉三角为例分析一个list的切片与拷贝
在triangles1中yield每次返回对象res,在for t in triangles1中t每次得到的是yield返回的变量即t=res,此处是变量赋值,两个变量指向同一空间,因此最终result中每个元素都指向同一空间,而triangles1中每次操作都会改变该对象的值
'''
