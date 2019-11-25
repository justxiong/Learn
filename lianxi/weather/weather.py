# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from weatherui import *

import json
import requests


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.provincelist=set([])
        self.citylist={}
        self.citys=[]
        self.get_province_data()
        self.cmbPro.addItems(self.provincelist)
        self.
        self.cmbPro.activated[str].connect(self.select_province)

    def get_province_data(self):
        #self.textEditShowcity.clear()
        with open('./cn_weather_citylist.json') as f:
            self.json_data=json.load(f)
            for i in self.json_data:
                self.provincelist.add(i['province'])


    def select_province(self,pro):
        self.textEditShowcity.clear()
        for i in self.json_data:
            if pro == i['province']:
                self.citylist[i['cityName']]=i['cityCode']
                self.citys.append(i['cityName'])
        self.cmbCity.addItems(self.citys)
        self.cmbCity.activated[str].connect(self.get_weather_data)

    def get_weather_data(self,city):
        citycode=self.citylist[city]
        url='http://www.weather.com.cn/data/sk/'+citycode+'.html'
        req=requests.get(url)
        req.encoding='utf-8'
        msg1 = '城市: %s' % req.json()['weatherinfo']['city'] + '\n'
        msg2 = '风向: %s' % req.json()['weatherinfo']['WD'] + '\n'
        msg3 = '温度: %s' % req.json()['weatherinfo']['temp'] + ' 度' + '\n'
        msg4 = '风力: %s' % req.json()['weatherinfo']['WS'] + '\n'
        msg5 = '湿度: %s' % req.json()['weatherinfo']['SD'] + '\n'
        self.textEditShowcity.setText(msg1+msg2+msg3+msg4+msg5)


if __name__=='__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())


