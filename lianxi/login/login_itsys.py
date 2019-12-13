#!/usr/bin/env python
# coding=utf-8

#https://www.jb51.net/article/141305.htm
#https://blog.csdn.net/zwq912318834/article/details/79571110
#https://blog.csdn.net/qq_35490191/article/details/80598620


import sys
import requests
import re
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import json
import datetime

s = requests.Session()
s.cookies = cookielib.LWPCookieJar(filename = "cookie.txt")
url_login = 'http://it.guoxintech.com/asset/users/check_login'
name=input('用户名:')
passwd=input('密码:')
formdata = {
'login': name,
'pwd': passwd,
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
r = s.post(url_login, data=formdata,headers=headers)
try:
    user_info=BeautifulSoup(r.content,'html.parser').find('table').find('tr').find('td').contents[0]
except AttributeError as e:
    print('登录错误，无法获得用户信息')
    sys.exit(0)
print(user_info)
d1=d2=datetime.datetime.now().month
with open('./mydatainfo.txt','w') as f:
    while(d2-d1<3):
        d1=d1-1
        r = s.get('http://it.guoxintech.com/asset/wtime/getUserWtime/2019/'+str(d1+1),headers=headers)
        soup=BeautifulSoup(r.content,'html.parser').find('table').find_all('tr')
        for i in soup:
            if i != soup[len(soup)-1]:
                l=i.find_all('td')
                print('日期:{} 上班时间{} 下班时间:{} 工时:{}'.format(l[0].string,l[3].string,l[4].string,l[12].get_text().strip()))
                f.write('日期:{} 上班时间{} 下班时间:{} 工时:{} \n'.format(l[0].string,l[3].string,l[4].string,l[12].get_text().strip()))



