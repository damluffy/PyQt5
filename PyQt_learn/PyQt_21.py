# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:07:34 2018

进度条

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QPushButton,QProgressBar)

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.pbar=QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)
        
        self.btn=QPushButton('Start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)
  
        self.timer=QBasicTimer()
        self.step=0
        
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('QProgressBar')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def timerEvent(self,e):
        
        if self.step>=100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        self.step=self.step+1
        self.pbar.setValue(self.step)
        
    
    def doAction(self):
        
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100,self)
            self.btn.setText('Stop')

            
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