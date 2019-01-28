# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:38:41 2018

输入对话框

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QPushButton,QLineEdit,QInputDialog)
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.btn=QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le=QLineEdit(self)
        self.le.move(130,22)
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Input Dialog')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def showDialog(self):
        
        text,ok=QInputDialog.getText(self,'Input Dialog','Enter your name:')
        if ok:
            self.le.setText(str(text))
    
   
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