# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:22:26 2018

日历组件

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QMessageBox,QDesktopWidget,
                             QLabel,QCalendarWidget)

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        cal=QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20,20)
        cal.clicked[QDate].connect(self.showDate)
        
        self.lbl=QLabel(self)
        date=cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130,260)
        
        
        self.resize(500,500)
        self.center()   #设置居中
        
        self.setWindowTitle('Calendar')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def showDate(self,date):
        
        self.lbl.setText(date.toString())
        

            
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