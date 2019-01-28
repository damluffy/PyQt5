# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:12:02 2018

复选框

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        cb=QCheckBox('Show Title',self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)    
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('QCheckBox')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def changeTitle(self,state):
        
        if state==Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
    
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