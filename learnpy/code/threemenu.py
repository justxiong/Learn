#!/usr/bin/env python
# coding=utf-8
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
current_layer= menu
parent_list = []
while True:
    print('Current layer has')
    if not current_layer:
        print('Current layer no content')
    else:
        for i in current_layer:
            print('{element}'.format(element=i))
    choice=input('输入地址，b返回上一层，q退出程序').strip()
    if len(choice) == 0:
        continue
    elif choice == 'q':
        break
    elif choice == 'b':
        if len(parent_list) !=0 :
            current_layer = parent_list.pop()
        else:
            print('Now in top')
    elif choice in current_layer:   #多重字典时只判断是否在第一层
        parent_list.append(current_layer) #[{'北京':'xxx','上海':'xxx','山东':'xxx'}]
        #for i in parent_list:
        #    print('parent list is {ele}'.format(ele=i))
        current_layer = current_layer[choice]           #choice== '上海' {'闵行':'xxx','闸北':'xxx',xxx}
    else:
        print('no choice')




































