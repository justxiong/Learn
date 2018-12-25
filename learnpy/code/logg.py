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



#logging提供四个基础类用于日志记录
import logging
logger=logging.getLogger()#创建root logger
#logger.setLevel(loggin.INFO)
fh=logging.FileHandler('test.txt')  #输出到指定文件
ch=logging.StreadHandler()  #输出到终端
#fh.setLevel(lel)
#只能设置高于等于logger.setLevel，否则无效.有效则最终是该lel级，无效是logger.setLverl级
formatter=logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
logger.debug('xxxx')
logger.error('xxxx')

'handler用于发送相关信息到指定目的地,可以到控制台,网络,文件也可以自行构造handler'
#fh=logging.handlers.RotatingFileHandler(xxx) 可以管理日志文件大小

#filter组件
'''
filter=logging.Filter('abc')#过滤出以abc开头的log
logger.addFilter(filter) 或
handler.addFilter(filter)
也可以实现自定义过滤内容    class IgnoreBackupLogFilter(logging.Filter):
'''

