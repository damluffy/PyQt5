# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:47:44 2018

分割框

@author: ai-pc
"""
import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QFrame,QSplitter,QStyleFactory,QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        hbox=QHBoxLayout(self)
        
        topleft=QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        
        topright=QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        
        bottom=QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        
        splitter1=QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        
        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
           
        self.resize(500,500)
        self.center()   #设置居中
        
        self.setWindowTitle('Splitter')
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
