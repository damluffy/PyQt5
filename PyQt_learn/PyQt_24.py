# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:37:47 2018

单行文本编辑框

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QLabel,QLineEdit)

from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.lbl=QLabel(self)
        qle=QLineEdit(self)
        
        qle.move(60,100)
        self.lbl.move(60,40)
        
        qle.textChanged[str].connect(self.onChanged)
        
        
        self.resize(500,500)
        self.center()   #设置居中
        
        self.setWindowTitle('Calendar')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def onChanged(self,text):
        
        self.lbl.setText(text)
        self.lbl.adjustSize()
    
            
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