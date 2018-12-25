#!/usr/bin/env python
# coding=utf-8

#logging是python内置的标准模块，主要用于输出运行日志，可以设置日志的等级，路径等
#logging主要有四个部分:
'''
loggers 应用程序接口
handlers 指定日志位置
filters 对日志输出过滤
formatters 输出格式
'''
import logging

logging.warning('warning message')
logging.basicConfig(filename='example.log',level=logging.INFO)
logging.basicConfig(format = '%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p;',
    filename='example.log',level=logging.INFO)

