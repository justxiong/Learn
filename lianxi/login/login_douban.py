#!/usr/bin/env python
# coding=utf-8

#https://www.jb51.net/article/141305.htm
#https://blog.csdn.net/zwq912318834/article/details/79571110
#https://blog.csdn.net/qq_35490191/article/details/80598620



import requests
import re
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import json

s = requests.Session()
s.cookies = cookielib.LWPCookieJar(filename = "cookie.txt")
url_login = 'https://accounts.douban.com/j/mobile/login/basic'
name=input('用户名:')
passwd=input('密码:')
formdata = {
'name': name,
'password': passwd,
}
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Referer': 'Referer: https://accounts.douban.com/passport/login'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

r = s.post(url_login, data=formdata,headers=headers)
print('Status code {}'.format(r.status_code))
print('Content {}'.format(r.text))
print('url {}'.format(r.url))
s.cookies.save()
content=json.loads(r.text)

if(content['status']=='failed' and content['message']=='captcha_required'):
    print('需要验证码，稍后再试')
    #print('点击下面链接获取验证码 {url}'.format(url=content['payload']['captcha_image_url']))
    #captcha_text = input('Please input the captcha:')
    #formdata['captcha-solution'] = captcha_text
    #formdata['captcha-id'] = content['payload']['captcha_id']
    #r = s.post('https://accounts.douban.com/j/mobile/login/basic', data=formdata, headers=headers)


my_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
my_url='https://www.douban.com/people/207840771/'
my_info = s.get(my_url,headers=my_header)
my_info = BeautifulSoup(my_info.content, 'html.parser').find(id='db-usr-profile').select('.info')[0].find(name='h1').contents
print(my_info[0].strip())
'''
soup = BeautifulSoup(r.text, 'html.parser')
captcha = soup.find('img', id='captcha_image')#当登陆需要验证码的时候
if captcha:
    captcha_url = captcha['src']
    re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
    captcha_id = re.findall(re_captcha_id, content)
    print(captcha_id)
    print(captcha_url)
    captcha_text = input('Please input the captcha:')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    my_info = s.post(my_url, data=formdata, headers=my_headers)
'''


