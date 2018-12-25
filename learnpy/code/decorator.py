#!/usr/bin/env python
# coding=utf-8


'''装饰器其实就是一个以函数作为参数并返回一个替换函数的可执行函数。本质上就是一个函数，该函数用来处理其他函数，它可以让其他函数在不需要修改代码的前提下增加额外的功能，装饰器的返回值也是一个函数对象，它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等应用场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用装饰器其实就是一个以函数作为参数并返回一个替换函数的可执行函数。本质上就是一个函数，该函数用来处理其他函数，它可以让其他函数在不需要修改代码的前提下增加额外的功能，装饰器的返回值也是一个函数对象，它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等应用场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用'''

import time

#装饰器原理
def show_time(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print('spend %s'%(end_time-start_time))

    return wrapper


def foo():
    print('hello foo')
    time.sleep(3)

foo=show_time(foo)
foo()

#@符号是装饰器的语法糖,使用@
@show_time   #foo=show_time(foo)
def foo():
    print('hello foo')
    time.sleep(3)


@show_time  #bar=show_time(bar)
def bar():
    print('in the bar')
    time.sleep(2)

foo()
print('***********')
bar()

#带参数的被装饰函数
import time

def show_time(func):

    def wrapper(a,b):
        start_time=time.time()
        func(a,b)
        end_time=time.time()
        print('spend %s'%(end_time-start_time))

    return wrapper

@show_time   #add=show_time(add)
def add(a,b):

    time.sleep(1)
    print(a+b)

add(2,4)


#类装饰器
#函数名　__name__属性的functools.wraps模块

