# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:17:39 2018

字体选择框

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QPushButton,QLabel,QFontDialog,QSizePolicy,QVBoxLayout)
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        vbox=QVBoxLayout()
        
        btn=QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)
           
        self.lbl=QLabel('KnowLedge only matters',self)
        self.lbl.move(130,20)
        
        vbox.addWidget(btn)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Color Dialog')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def showDialog(self):
        
        font,ok=QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
    
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