#!/usr/bin/env python
# coding=utf-8



a=10


def f():
    a=2
    a=a+10
    return a

print ("f is %d"%f())
print ("a is %d"%a)
print ("f is %d"%f())
