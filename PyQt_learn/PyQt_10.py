# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:15:24 2018

信号和槽机制
@author: ai-pc
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QLCDNumber,QSlider,QVBoxLayout)
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        lcd=QLCDNumber(self)
        sld=QSlider(Qt.Horizontal,self)
        
        vbox=QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        
        self.setLayout(vbox)
        
        sld.valueChanged.connect(lcd.display)
                                
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Signal & Slot')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    
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