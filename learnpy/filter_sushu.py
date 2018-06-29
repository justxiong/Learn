#!/usr/bin/env python
# coding=utf-8
def _odd_iter():
    s=1
    while True:
        s=s+2
        print ('get s %d',s)
        yield s

def _not_divisible(n):
    return lambda x: x%n>0

def primes1():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        #filter第一个参数是函数,此处使用了匿名函数
        it=filter(_not_divisible(n),it)

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        #等价与
        f=_not_divisible(n) #f指向_not_disible中的匿名函数,f可以认为是函数名,
        it=filter(f,it)#第一个参数是函数(名),而不是函数的调用,让f即lambda作用于序列
            #如果不使用匿名函数,此时filter中第一个参数函数只会依次处理序列中元素,即该函数只能依次接收序列中元素作为参数,而无法接收其它参数,但该函数的功能又需要序列的第一个元素,这就只能使用全局变量实现
#全局变量实现
first=0
def _not_divisible2(n):
    global first
    print ('div get n is %d first id %d'%(n,first))
    return n%first>0

def primes2():
    global first
    yield 2
    it=_odd_iter()
    while True:
        first=next(it)#拿出序列第一个元素后,序列就不再包含第一个元素
        yield first
        #filter第一个参数是函数,此处使用了匿名函数
        it=filter(_not_divisible2,it)   #会循环嵌套调用

#for遍历gererator
for n in primes2():
    if n<10:
        print(n)
    else:
        break
