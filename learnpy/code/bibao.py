#!/usr/bin/env python
# coding=utf-8

'闭包'
'    一般程序中,一个函数结束时,会将自己的临时变量释放,但闭包实现方式是如果内部函数有使用自己的局部变量,则将这些变量与内层函数绑定到一起,即使外层函数结束,调用内层函数仍然能够使用外层函数的临时变量,这些变量也称为闭包变量'

'典型闭包格式'
'   闭包格式:在一个函数中再定义一个函数,且外层函数的参数和变量可以保存在内层函数中,外层函数返回内层函数,调用首先得到的是内层函数,而不是内层函数调用的结果.'
'   1: 闭包函数一定要注意内层函数中的"外部变量",包括模块的全局变量,外层函数的临时变量和外层函数中循环变量'
'   2: 每次调用闭包函数都将返回一个新的函数,即使传入相同参数f1 = lazy_sum(1, 3, 5) f2 = lazy_sum(1, 3) f1 != f2'

'闭包应用'
'   装饰器,面向对象,单利模式,https://www.cnblogs.com/Lin-Yi/p/7305364.html'

print('test 闭包')

print('test 闭包-模块变量 begin')
def f1():
    def f2(j):
        return m*j
    return f2
m=1
f=f1()
print(f(3))
m=m+1
print(f(3))

def f1():
    def f2(j):
        global m
        m=m+1
        return m*j
    return f2
m=1
f=f1()
print(f(3))
print(f(3))
print('test 闭包-模块变量 end')

print('test 闭包-外函数变量/闭包变量 begin')
#def f1(m): //same
def f1():
    m=1
    def f2(j):
        nonlocal m
        m=m+1
        return j*m
    return f2
f=f1()
print(f(3))
print(f(3))
#!!!!!!!!!!!!!!!!!!!
'闭包函数返回内层函数引用，同一个内层函数的引用调用都将使用一份闭包变量(内层函数的局部变量)，第二次调用f(3)与第一次f(3)使用了相同的闭包变量，所以第二次调用时m的值已变为2.从另一个角度理解m对于内层函数而言此时是“全局变量”，函数中修改且使用该全局变量因此结果不同'
#!!!!!!!!!!!!!!!!!!!
ff=f1()
print(f==ff)    #false 闭包函数每次调用返回一个新函数(引用)
print(ff(3))
#!!!!!! 闭包函数每次调用返回新函数，因此f!=ff,且此时也将获得新的独立闭包变量，即得到新的m=1,而不是延续上面的值

print('test 闭包-外函数变量/闭包变量 end')



print('test 闭包-循环变量 begin')
'由于闭包变量与内层函数的关联，在外层函数的for循环中实现内层函数又会更复杂,即'

fs = []
for i in range(6):
    fs.append(lambda j:i*j)
print([f(2) for f in fs])
#上下两种写法等价,上面这种格式也相当于完成了一次闭包调用，但没有下面方式清晰，需要注意!!!!!!!!!!
def f1():
    fs=[]
    for i in range(6):
        def f2(j):
            return i*j
        fs.append(f2)
    return fs
f=f1()
#f==[f2,f2,f2,f2,f2,f2]
for i in range(6):
    #print(f[i](i))
    print(f[i](2))
'关键点:for循环中只是定义函数而不是调用函数，因此i不会立即取值，只有最终调用时才会取值.调用时由于内部没用定义i,因此到上一级找i,而此时i以变为5,类似于函数中使用全局变量，在函数调用前全局变量发生了变化，最终调用函数会取该全局变量此时的值而不是函数定义时全局变量的值'
'由于只有一次闭包调用，因此所有返回内层函数的引用都将使用同一份闭包变量i,而在调用内层函数过程中闭包变量没有再发生改变，都是5.'

'''m=5
#def f():
    #m=m+1
    return m*m
m=m+1
f()
原理类似，只有在函数最终调用时，函数中没有定义的局部变量才取到上层同名变量的值.只限读取而不能修改如a'''

'如果非要取得1循环变量的值可采用下面方式'
def f1():
    fs=[]
    def f2(i):
        def f3(j):
            return i*j
        return f3
    for i in range(6):
        fs.append(f2(i))
    return fs
f=f1()
#f==[f2,f2,f2,f2,f2,f2] #此处的各个f2
for i in range(6):
    print(f[i](2))

'此时由于是f2构成闭包，闭包变量是f2中的局部变量i,而fs.append(f2(i))是函数调用，此时函数f2中局部变量i将会取得外层i的值，即for中012...．根据原则2,for中每次调用闭包函数,都返回新函数(新的内层函数引用)，每个新函数都有一份独立的闭包变量i，最终每个内层函数调用时将使用各自的闭包变量i，在i=012..时分别定义了内层函数且在内层函数调用前各自闭包变量没有变化，最后调用时内层函数的闭包变量将分别取得各自外层函数外层的i=012...
即在i=012...时依次得到内层函数的引用，因此最终内层函数调用时闭包变量分别取的对应值
而不是和上面一样只有一个新函数和一份闭包变量，而最终使用同一个闭包变量i=5'
def hellocounter(name):
    count = [0]     #对于可变类型数据变量内层函数可以直接读写
    def counter():
        count[0] += 1
        print("hello ",name , ',',str(count[0])+'access!')
    return counter

hello = hellocounter('make_program')
hello()
hello()
hello()
#这个与for循环例子的差别:都只有一次闭包调用，因此是公用一份闭包变量，for循环中是外层函数的for循环不断改变闭包i的值，因此最终调用内层函数时闭包变量i的值已变为5在后面内层函数调用过程中该闭包变量则一直没有改变
#而这里只有在内层函数中改变了闭包变量，即只有内层函数发生调用时闭包变量才会改变，每次调用时使用闭包变量都会收到前一次影响,类似于函数中会修改全局变量，那两次相邻相同函数调用结果将不同

print('test 闭包-循环变量 end')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
'''闭包函数:
     一次闭包调用所获得的内层函数引都用使用同一份闭包变量，闭包变量值取决于调用内层函数时的取值，调用内层函数时闭包变量的值可能与定义时发生了改变(两种常见改变:1如外层函数在for中定义内层函数时就不断改变闭包变量i，最终内层函数调用时i=5,第一个for例子,2如hellocounter例子中内层函数自己改变了闭包变量导致同一个内层函数引用的多次调用结果将不同)
    而多次调用闭包函数将获得多个内层函数的引用且各自闭包变量独立，此时闭包变变量是不会受到各个闭包函数调用的影响，只要在该内层函数定义完到调用期间自己的闭包变量没有改变，则该闭包变量的值就是定义时的值,第二个for例子.

    !!!!!!闭包变量对内层函数而言是'全局变量'，而内层函数的定义引用都不会操作该变量(不读不写)，只有在内层函数调用时会到外层函数查找并1使用该变量'

'''
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#











print('test 闭包与匿名函数 begin')
'由于闭包涉及到函数内部定义函数，常采用匿名函数格式'

def f3(i):
    def f4(j):
        return i*j
    return f4
f=f3(3)
print(f(5))
#闭包函数的匿名函数格式
f3=lambda i:lambda j:i*j
f=f3(3)
print(f(5))


'上面for循环例子中函数f1的功能是将函数f2依次加入到列表中,这可以使用列表生成式实现,其中函数f2由可以借助匿名函数实现'
fs=[lambda j:i*j for i in range(6)]
print([f(2) for f in fs])
'与上面例子中函数等价，但采用匿名函数，代码更简洁'

print('test 闭包与匿名函数 end')


print('综合应用begin，闭包,匿名函数，map')


def f3(i):
    def f4(j):
        return i*j
    return f4

fns=map(f3,range(6))
print([f(2) for f in fns])
'!!!!!!!!!!!!!!!!闭包函数每次调用返回新函数，每个新函数中使用独立的闭包变量，map函数是将f3依次作用于后面6个参数，即有6次闭包调用，每个新函数(引用)中使用独立的闭包变量，该闭包变量依次取得对应外层函数的i值,因此最后内层函数调用时会依次取得每个i值，而不是共用一份闭包变量'
#采用匿名表达式写法
fs=map(lambda i: lambda j:i*j,range(6))
print([f(2) for f in fs])


fs = [(lambda i:lambda j:i*j)(i) for i in range(6)]
print([f(2) for f in fs])
#lambda i:lambda j:i*j 等价于闭包函数名f3，后面跟(i)表示闭包函数的调用，因此是在for循环中调用闭包函数，与上面map等价
#格式相似的有


fs = []
for i in range(6):
    fs.append(lambda j:i*j)
print([f(2) for f in fs])
#上下两种写法等价
fs = [(lambda j:i*j) for i in range(6)]
print([f(2) for f in fs])
#此时,这种写法是上面for循环中例子，等价于调用一次闭包，内层函数调用使用一份闭包变量





# 用途1：当闭包执行完后，仍然能够保持住当前的运行环境。
# 比如说，如果你希望函数的每次执行结果，都是基于这个函数上次的运行结果。我以一个类似棋盘游戏的例子
# 来说明。假设棋盘大小为50*50，左上角为坐标系原点(0,0)，我需要一个函数，接收2个参数，分别为方向
# (direction)，步长(step)，该函数控制棋子的运动。棋子运动的新的坐标除了依赖于方向和步长以外，
# 当然还要根据原来所处的坐标点，用闭包就可以保持住这个棋子原来所处的坐标。

origin = [0, 0] # 坐标系统原点
legal_x = [0, 50] # x轴方向的合法坐标
legal_y = [0, 50] # y轴方向的合法坐标
def create(pos=origin):
 def player(direction,step):
  # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
  # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。
  new_x = pos[0] + direction[0]*step
  new_y = pos[1] + direction[1]*step
  pos[0] = new_x
  pos[1] = new_y
  #注意！此处不能写成 pos = [new_x, new_y]，原因在上文有说过
  return pos
 return player

player = create() # 创建棋子player，起点为原点
print (player([1,0],10)) # 向x轴正方向移动10步
print (player([0,1],20)) # 向y轴正方向移动20步
print (player([-1,0],10)) # 向x轴负方向移动10步


