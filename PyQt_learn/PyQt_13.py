# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:50:26 2018

发送信号
@author: ai-pc
"""

import sys
from PyQt5.QtCore import Qt,pyqtSignal,QObject
from PyQt5.QtWidgets import (QMainWindow,QApplication,QMessageBox,QDesktopWidget)
from PyQt5.QtGui import QIcon


class Communicate(QObject):
    
    closeApp=pyqtSignal()


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.c=Communicate()
        self.c.closeApp.connect(self.close)
        
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Sender')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def mousePressEvent(self,event):
        
        self.c.closeApp.emit()
    
    
    def keyPressEvent(self,e):       #重写事件处理函数
        
        if e.key()==Qt.Key_Escape:   #点击esc按钮，应用被终止
            self.close()
       
   
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