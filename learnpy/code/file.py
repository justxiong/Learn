#!/usr/bin/env python
# coding=utf-8

#os模块
#python内置的os模块可以直接调用操作系统提供的接口函数
#操作文件和目录的函数一部分放在os中，一部分放在os.path中
#os.path.abspath('.')  当前目录绝对路径
#os.path.join('/user/xj','test') 合并路径
#os.mkdir('/user/xj/test')
#os.rmdir('/user/xj/test')
#os.path.split('/user/xj/test.txt') 得到('/user/xj','test.txt')
#os.path.splitext('/user/xj/test.txt') 得到('/user/xj/test','txt')
#os模块不提供复制功能，shutil模块提供复制功能，也可以使用文件读写来实现
#shutil.copyfile(src,dst)
#shutil是高级的文件，文件夹，压缩包处理模块，提供以一系列相关操作的功能函数

#os模块提供了os.system可以调用shell命令如，os.system('cp test.txt test1.txt')

#sys模块
#sys.argv[0] 程序自身名字，1,2,3...依次是传入的参数,len(sys.argv)参数个数加自身名字
#sys.exit(0)
#sys.path python模块搜索路径，sys.path.append('xxx')

#python执行shell命令或脚本
#常见的有os.system.commands.popen2等，如os.system('cp test.txt test1.txt')
#官方提供subprocess模块，用于统一实现对系统命令或脚本的调用
#常见用法subprocess.run('rm test1.txt',shell=True)



#这几个系统模块更多信息　https://www.cnblogs.com/wj-1314/p/8557077.html



''''文件读写操作'''

#f.write/writeline(str) 默认不会带换行
#!!!! r模式只有文件存在才行，w,a在文件不存在时会自动创建同名文件!!!!!!!!!!!!
'''
    r       只读 默认模式
    r+      读写，指针在开头，写多少覆盖多少，原内容可能有部分保留
    w       只写，写入内容会将原内容全部覆盖
    w+      读写，写入内容将原内容全覆盖
    a/a+    追加，带读功能的追加，由于指针在文尾，读到的也是''
    b       二进制，以二进制格式打开一个文件用于读，写，追加(rb,wb,ab)
'''

#r 文件不存在时会报错，可采用下面两种方法检测或新建文件
if not os.path.exists('/tmp/userstate.txt'):
    os.mknod('/tmp/userstate.txt')#only linux

try:
    with open('/tmp/userstate.txt','r+') as userstate:
        name_list = userstate.read()
        if username in name_list:
            print('user has locked')
            break;
except FileNotFoundError as e:
    os.mknod('/tmp/userstate.txt')#only linux

#文件不存在时也可以利用w/a自动创建来创建文件
    open('/tmp/userstate.txt','w+') as userstate:


#文件夹操作
if not os.path.isdir('./test'):
    os.mkdir('./test')

'''
s=f.readline()从文件中读取一行，含行结束符，s=0表示到文件尾
s=f.readlines()依次从文件中读取每一行，s是含每一行的列表
'''


#一种文件修改常用操作
with open('file.txt','r') as oldfile:
    with open('newfile.txt','w') as newfile:
        for line in f/f.readline():
            #按行读取，较少内存消耗
            if oldline in line:
                #将line中line中需要修改部分替换
                line=line.replace(oldline,newline):
            newfile.write(line)

os.replace('newfile.txt','file.txt')

#result = chardet.detect(open('log',mode='rb').read()) 探测文件编码类型
#seek相关
f.seek(n,0) ,f.seek(n,1),f.seek(n,2)    #分别从头，当前，尾部移动n个字节
#f.truncate()　#可写模式下，将文件从当前位置剪裁，后面部分将裁掉


#读取一个文件夹下所有文件
dir_path='/home/xiongjian'
#得到指定目录下所有文件
file_list = os.listdir(dir_path)
for i in file_list:
    #每个文件的完整路径
    path = os.path.join(dir_path,i)
    print(path)

#
f = open('poem.txt', 'r+', encoding='utf-8')
f.seek(3*n)     #对于utf-8而言，汉字是3个字节编码，因此，每个汉字需要移位3
f.read(1)   #读取光标后一个汉字，光标后移3,而不是读取一个字节，后移1





#序列化
'''把变量从内存中变成可存储或传输的过程称为序列化，序列化后的内容可以写入磁盘或通过网络传输，反之把变量内容从序列化的对象重新读到内存里称为反序列化
    python提供pickle模块实现序列化
    d = dict(name='Bob', age=20, score=88)
    pickle.dumps(d)		//把任意对象序列化成一个bytes,然后可以写入文件
    d = pickle.loads(f)	//反序列化出对象'''
    #pickle是处理bytes数据，因此文件open的模式必须有'b'

#由于文件只能以字符串和二进制方式写入(当然都是以二进制格式写入到硬盘)，因此内存中数据要保存到文件需要先序列化
#pickle 是专门针对python设计，支持所有python数据类型，但也只能在python中使用，而json只支持python中str,int,list,tuple,dict类型，但可以在多种语言中使用

#json
    '''json的标准对象是js对象，与python内置数据类型存在对应关系
json格式表示出来的是一个字符串，可以被所有语言读取，也可以方便存储和传输
json格式是字符串对象可按字符串方法处理该对象，反序列化后变为js对象/python中对应一种对象，可按该对象的方法处理

    python中提供json模块
        d = dict(name='Bob', age=20, score=88)
        json.dumps(d)
        json.dumps(d,f) #f=open('xxxxx')
        dumps/dump前者返回一个str,内容是标准的json,后者可以直接把json写入一个file-like object
        json_str = '{"age": 20, "score": 88, "name": "Bob"}'
        json.loads(json_str)
        json.load(f) #f=open('xxxx'),即直接读取file-like内容并反序列化
        loads/load前者把json的字符串反序列化，后者从file-like object中读取字符串并反序列化

        dumps/loads方法无法直接将实例序列化/反序列化
            这个的处理机制是借用{}字典这个中间对象实现转换
            json.dumps(s, default=lambda obj: obj.__dict__)
               default默认接收一个函数，该函数会先处理传入的实例．由于实例中特殊变量__dict__保存该实例的变量，因此借助这个可以将实例变为dict然后序列化．
                同样loads也是将一个json对象反序列化为dict,要将该dict进一步变为实例也需要借助函数，在函数中根据该dict内容重新获得对象．
            json.loads(json_str, object_hook=dict2student)
                dict__只保存实例变量没有方法，反序列后得到的是dict，dict中是这些变量信息，需要借助这行变量重新初始化类得到新的实例，只是这个新实例与原实例有相同变量

    json只是以字符串形式保存信息，序列化前的对象与反序列花后的对象间没有内在关系，只是有相同的内容而以
'''


#StringIO即在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())
getvalue()#方法用于获得写入后的str

f = StringIO('Hello!\nHi!\nGoodbye!')
s = f.readline()

#BytesIO用于在在内存中读写二进制数据bytes
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))	//写入的不是str而是进过utf-8编码的bytes
f.read()


#python中shelve模块也提供了序列化功能
#python中提供 xml.etree.ElementTree as ET模块处理xml文档
