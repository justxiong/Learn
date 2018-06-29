#!/usr/bin/env python
# coding=utf-8



from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        #super(LastUpdatedOrderedDict, self).__init__()
        #super().__init__()  #借用父类OrderedDict初始化self,因此创建的对象类似dict
        OrderedDict.__init__(self)
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0   #dict属性，判断key是否在dict中
        if len(self) - containsKey >= self._capacity:   #dict属性，len(dict)
            last = self.popitem(last=False)#last false fifo,true lifo
            print('remove:', last)  #popitem与dict中不同，即OrderedDict中对popitem方法有所改动
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

obj=LastUpdatedOrderedDict(2)
obj['name']='xiongjian'
print (obj['name'])
