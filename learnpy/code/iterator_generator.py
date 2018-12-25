#!/usr/bin/env python
# coding=utf-8

#列表生成式 [表达式]
[i+1 for i in l]
[d for d in os.listdir('.')]

#generator
g = (x * x for x in range(10))
for n in g:
    print (n)

def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'

for i in fib(6):
    print(i)

g=fib(6)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e.value)  #done
        break

#利用yield实现一个协程
def consumer(name):
    print("%s 准备学习啦!" %name)
    while True:
       lesson = yield

       print("开始[%s]了,[%s]老师来讲课了!" %(lesson,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("同学们开始上课 了!")
    for i in range(10):
        time.sleep(1)
        print("到了两个同学!")
        c.send(i)
        c2.send(i)

#迭代器iterator

