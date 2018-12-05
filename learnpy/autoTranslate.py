#!/usr/bin/env python
# coding=utf-8

#需要第三方模块sudo pip install xxx

import requests
import json
import sys
from bs4 import  BeautifulSoup
import re
import execjs
import os
import urllib
import xlwt
import xlrd
from xlutils.copy import copy

XLS_FILE_PATH='../../theme/linux/language/i18n.xls'

gettkJsCode='''function b(a, b) {
  for (var d = 0; d < b.length - 2; d += 3) {
      var c = b.charAt(d + 2),
          c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
          c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
      a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
  }
  return a
}

function tk(a,TKK) {
    for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
        var c = a.charCodeAt(f);
        128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ? (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240, g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
    }
    a = h;
    for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
    a = b(a, "+-3^+b+-f");
    a ^= Number(e[1]) || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1E6;
    return a.toString() + "." + (a ^ h)
}'''


class Translate:
    def __init__(self,input_str,tolangs,output_path):
        self.input_str=input_str
        self.output_str_list=[]
        self.output_path=output_path
        self.temp_dir="/tmp/translate"
        self.tolangs=tolangs
        if not os.path.exists("/tmp/translate"):
            os.mkdir("/tmp/translate")


    def __del__(self):
        os.system("rm -rf /tmp/translate")

    def getgoogletk(self):
        part_jscode_2="\n"+"return TKK;"
        tkk_page=requests.get('https://translate.google.cn',headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0"})
        tkk_code=BeautifulSoup(tkk_page.content,'lxml')
        patter= re.compile(r'(TKK.*?\);)', re.I | re.M)
        part_jscode=re.findall(patter,str(tkk_code))
        js_code=part_jscode[0]+part_jscode_2
        with open (self.temp_dir+"/gettkk.js","w")  as  f1:
            f1.write(js_code)
            f1.close
        tkk_value=execjs.compile(open(self.temp_dir+"/gettkk.js").read()).call('eval')
        with open (self.temp_dir+"/gettk.js","w")  as  f2:
            f2.write(gettkJsCode)
            f2.close

        tk_value=execjs.compile(open(self.temp_dir+"/gettk.js").read()).call('tk',self.input_str,tkk_value)
        self.tk=tk_value
        #print "tk value is "+tk_value


    def extract_translation(self):
        for lan in self.tolangs:
            url='https://translate.google.cn/translate_a/single?client=t&sl=en&tl='+lan+'&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&ssel=0&tsel=3&kc=0&tk='+self.tk+'&q='+urllib.quote(self.input_str)
            #print (url)
            req = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0"})
            res=req.json()[0][0][0]
            print res
            self.output_str_list.append(res)
        print self.output_str_list

    def write_into_xls(self):
        rb=xlrd.open_workbook(self.output_path,formatting_info=True)
        wb=copy(rb)
        ws=wb.get_sheet(0)
        sh = rb.sheet_by_index(0)
        nrows = sh.nrows
        ncols = sh.ncols
        print "old xls rows = %d; cols = %d" % (nrows, ncols)
        font=xlwt.Font()
        font.height=240
        borders=xlwt.Borders()
        borders.top=6
        style=xlwt.XFStyle()
        style.font=font

        ws.write(nrows,0,self.input_str,style)
        for i in range(1,len(self.output_str_list)+1):
            ws.write(nrows,i,self.output_str_list[i-1],style)
        wb.save(self.output_path)

    def run(self):
        self.getgoogletk()
        self.extract_translation()
        self.write_into_xls()


if __name__ == "__main__":
    if len(sys.argv)<2:
        print ('eg:python autoTranslate.py hello world')
        sys.exit()
    input_words=''
    for j in range(1,len(sys.argv)):
        if j!=len(sys.argv)-1:
            input_words+=sys.argv[j]+' '
        else:
            input_words+=sys.argv[j]
    #print (input_words)
    tolangs=['en','ar','fa','fr','es','pt','tr','vi','ru','de','th']

    transword=Translate(input_words,tolangs,XLS_FILE_PATH)
    transword.run()






#https://blog.csdn.net/yingshukun/article/details/53470424
