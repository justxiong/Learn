#!/usr/bin/env python
# coding=utf-8

#https://blog.csdn.net/qq_35490191/article/details/80598620


import requests
from bs4 import BeautifulSoup
import json
count=0
info_url='https://usdawatercolors.nal.usda.gov/pom/search.xhtml?start='
for i in range(2):
    req=requests.get(info_url+str(i*20))
    soup=BeautifulSoup(req.content,'html.parser').find(id='documents').select('.document.blacklight-image')
    for i in soup:
        info=i.select('.defList')[0].contents
        while '\n' in info:
            info.remove('\n')
        pic_info=[]
        for i in info:
            if i.name == 'dt':
                pic_info.append(i.string)
            elif i.name == 'dd':
                if(i.find('a')==None):
                    pic_info.append(i.string)
                else:
                    pic_info.append(i.find('a').string)
            elif i.name == 'div' and i['class'][0]== 'defList2':
                img_id=i.find('a').find('img')['src'].split('/')[2]
                down_url='https://usdawatercolors.nal.usda.gov/pom/download.xhtml?id='+img_id
                print(down_url)
                img=requests.get(down_url)
                with open('./'+pic_info[pic_info.index('Scientific name:')+1]+'_'+img_id+'.json','w') as f:
                    f.write(json.dumps(pic_info))
                with open('./'+pic_info[pic_info.index('Scientific name:')+1]+'_'+img_id+'.jpg','wb') as f:
                    f.write(img.content)
