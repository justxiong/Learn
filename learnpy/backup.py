#!/usr/bin/env python
# coding=utf-8

#exerce backup.py

import os
import time
import sys

source=[]
if len(sys.argv)>1:
    for i in sys.argv:
        source.append(i)
else:
    source.append('/home/xiongjian/桌面/learn/支持')

#source=['/home/xiongjian/桌面/learn/支持','/home/xiongjian/桌面/test.c']
target_dir='/home/xiongjian/desktop/'+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print ('successful create dir')

comment=input('Enert a comment-->')
#py2 comment=raw_input('Enert a comment-->')
if(len(comment)==0):
    #target=target_dir+os.sep+now+'.zip'
    target=target_dir+os.sep+now+'.tar.gz'
else:
    #target=target_dir+os.sep+now+'_'+comment.replace(' ','_')+'.zip'
    target=target_dir+os.sep+now+'_'+comment.replace(' ','_')+'.tar.gz'
    #str.replace(' ','_')用下划线代替空格，每个空格都会替换
#os.sep根据操作系统指定分割符
#str.join以指定字符串将序列中元素(限于字符串)连成一个字符串
#zip_command="zip -qr '%s' %s"%(target,' '.join(source))
#excludes.txt文件中指定文件名的文件将不会打包压缩
#zip_command="tar -cvzf '%s' %s -X /home/xiongjian/桌面/excludes.txt" %(target,' '.join(source))
zip_command="tar -cvzf '%s' %s" %(target,' '.join(source))
print (zip_command)
#os.system 运行shell命令
#zip -qr 递归压缩
if os.system(zip_command)==0:
    print ('Successful back up to',target)
else:
    print ('Backupfailed')

