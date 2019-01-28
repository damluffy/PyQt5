# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:42:34 2018

滑块条
@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QSlider,QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QPixmap

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        sld=QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.changeValue)
          
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('silent.jpg'))
        self.label.setGeometry(150,20,100,100)
  
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('QCheckBox')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def changeValue(self,value):
        
        if value==0:
            self.label.setPixmap(QPixmap('silent.jpg'))
        elif value>0 and value<=30:
            self.label.setPixmap(QPixmap('min.jpg'))
        elif value>30 and value<80:
            self.label.setPixmap(QPixmap('mid.jpg'))
        else:
            self.label.setPixmap(QPixmap('max.jpg'))

        
    
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