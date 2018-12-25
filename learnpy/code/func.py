#!/usr/bin/env python
# coding=utf-8

#对于不可变类型变量
x=1
def func1():
    x=0 #声明函数局部变量，函数中将使用该局部变量，与外部变量互不影响
    x=x+1
    print(x)
func1()
print(x)

x=1
def func1():
    #x=x+1  #不申明则默认使用外部变量，只能读不能写,除非用global声明
    print(x)
func1()
print(x)

x=6
def f2():
    print(x)
    #x=5 #先使用后申明也不行,由于是先在函数内部查找，因此print中x是局部变量而不是外部x,但该局部变量在申明前使用会报错
f2()

#对于可变类型如list
l=[]
def func2():
    print(l)
    l.append(1) #不申明时使用外部变量，可读可写
    print(l)
func2()
print(l)

#内层函数使用外层函数的局部变量(嵌套作用域)
def outer():
    count = 10
    def inner():
        nonlocal count
        count = 20
        print(count)
    inner()
    print(count)
outer()
#对于内外层函数而言，外层函数的局部变量对于内层函数类似于全局变量与内层函数的关系



def fun3(s):
    al_num=0
    space_num=0
    digit_num=0
    others_num=0
    for i in s:
        if i.isdigit():
            digit_num+=1
        elif i.isalpha():
            al_num+=1
        elif i.isspace():
            space_num+=1
        else:
            others_num+=1
    print('alpha num is {al}, digit num is {di}, space_num is {sp}, other is {ot}'.format(al=al_num,di=digit_num,sp=space_num,ot=others_num))

result = fun3("asdsadjlk1212jdjakdk2  d d d d323233223下")


