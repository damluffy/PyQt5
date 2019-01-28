# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:21:49 2018
切换按钮

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QPushButton,QFrame)
from PyQt5.QtGui import QIcon,QColor

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.col=QColor(0,0,0)
        
        redb=QPushButton('Red',self)
        redb.setCheckable(True)
        redb.move(10,10)
        redb.clicked[bool].connect(self.setColor)
        
        greenb=QPushButton('Green',self)
        greenb.setCheckable(True)
        greenb.move(10,60)
        greenb.clicked[bool].connect(self.setColor)
        
        blueb=QPushButton('Blue',self)
        blueb.setCheckable(True)
        blueb.move(10,110)
        blueb.clicked[bool].connect(self.setColor)
        
        self.square=QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget {background-color: %s}' % self.col.name())
      
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('QCheckBox')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def setColor(self,pressed):
        
        source=self.sender()
        
        if pressed:
            val=255
        else: val=0
        
        if source.text()=='Red':
            self.col.setRed(val)
        elif source.text()=='Green':
            self.col.setGreen(val)
        else: self.col.setBlue(val)
     
        self.square.setStyleSheet('QFrame {background-color: %s}' % self.col.name())
        
    
    def center(self):   #居中函数
        
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center() 
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def closeEvent(self,event):
        
        reply=QMessageBox.question(self,'Message','Are you sure to quit?',
                                   QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        

if __name__=='__main__':
    
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())