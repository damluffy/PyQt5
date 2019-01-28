# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:58:41 2018

下拉列表框

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QLabel,QComboBox)

from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.lbl=QLabel('I choose: Power',self)
        
        combo=QComboBox(self)
        combo.addItem('Knowledge')
        combo.addItem('Peace')
        combo.addItem('Money')
        combo.addItem('Love')
        combo.addItem('Power')
        combo.addItem('Life')
        
        combo.move(50,50)
        self.lbl.move(50,150)
        
        combo.activated[str].connect(self.onActivated)
        
       
        self.resize(500,500)
        self.center()   #设置居中
        
        self.setWindowTitle('QComboBox')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def onActivated(self,text):
        
        self.lbl.setText('I choose: '+text)
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
