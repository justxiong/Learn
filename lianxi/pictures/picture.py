# -*- coding: utf-8 -*-

import sys,os
from PyQt5.QtWidgets import QApplication , QMainWindow
from mainWindow import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.labelImg.setText("选择图片")
        self.labelImg.setScaledContents(True)
        self.pictype=[".jpg",".png",".jpeg"]
        self.pics=[]
        self.ppMode="manual"
        self.timer=QTimer(self)

        self.btnSelect.clicked.connect(self.selectPic)
        self.btnPriv.clicked.connect(self.playPriv)
        self.btnNext.clicked.connect(self.playNext)
        self.btnPP.clicked.connect(self.ppMode)
        self.timer.timeout.connect(self.autoPlay)

    def selectPic(self):
        pic_filter=""
        for i in self.pictype:
            pic_filter=pic_filter+"*"+i+" "
        self.fname,_=QFileDialog.getOpenFileName(self,'Open file','/home',"Image files("+pic_filter+")")
        curDir=os.path.dirname(self.fname)+"/"
        for f in os.listdir(curDir):
            if os.path.splitext(f)[1] in self.pictype:
                self.pics.append(curDir+f)
        self.labelShowPic()

    def playPriv(self):
        if self.ppMode=="auto":
            self.timer.stop()
            self.ppMode="manual"
        index=self.pics.index(self.fname)
        if index==0:
            self.fname=self.pics[len(self.pics)-1]
        else:
            self.fname=self.pics[index-1]
        self.labelShowPic()

    def playNext(self):
        if self.ppMode=="auto":
            self.timer.stop()
            self.ppMode="manual"
        index=self.pics.index(self.fname)
        if index==len(self.pics)-1:
            self.fname=self.pics[0]
        else:
            self.fname=self.pics[index+1]
        self.labelShowPic()

    def ppMode(self):
        if self.ppMode=="manual":
            self.timer.start(2000)
            self.ppMode="auto"
        else:
            self.timer.stop()
            self.ppMode="manual"

    def autoPlay(self):
        self.playPriv()

    def labelShowPic(self):
        self.labelImg.setPixmap(QPixmap(self.fname))

if __name__=='__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())


