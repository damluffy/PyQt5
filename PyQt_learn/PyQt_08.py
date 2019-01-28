# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:24:50 2018

网格布局

@author: ai-pc
"""


import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QPushButton,QMessageBox,QDesktopWidget,
                             QGridLayout)
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        grid=QGridLayout()
        self.setLayout(grid)
        
        names=['Cls','Bck','','close',
               '7','8','9','/',
               '4','5','6','*',
               '1','2','3','-',
               '0','.','=','+']
        
        positions=[(i,j) for i in range(5) for j in range(4)]
        
        for position,name in zip(positions,names):
            if name=='':
                continue
            button=QPushButton(name)
            grid.addWidget(button,*position)
        
        
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