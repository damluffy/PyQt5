# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:19:44 2018

布局管理

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QMessageBox,QDesktopWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        okButton=QPushButton('Ok',self)
        cancelButton=QPushButton('Cancel',self)
        
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)

        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Just Exit')
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