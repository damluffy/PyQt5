# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:52:05 2018

颜色选择对话框
@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QPushButton,QFrame,QColorDialog)
from PyQt5.QtGui import QIcon,QColor

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        col=QColor(0,0,0)
        
        self.btn=QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        
        self.frm=QFrame(self)
        self.frm.setStyleSheet('QWidget {background-color:%s}' % col.name())
        self.frm.setGeometry(130, 22, 100, 100)  
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Color Dialog')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def showDialog(self):
        
        col=QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget {background-color:%s}' % col.name())
    
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