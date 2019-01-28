# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:00:04 2018

事件发送者
@author: ai-pc
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow,QApplication,QMessageBox,QDesktopWidget,
                             QPushButton)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        btn1=QPushButton('Hello',self)
        btn1.move(30,50)
        btn2=QPushButton('Hi',self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        
        
        self.statusBar()                        
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Sender')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def buttonClicked(self):
        
        sender=self.sender()
        self.statusBar().showMessage(sender.text()+' was pressed')
    
    
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