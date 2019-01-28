# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:43:37 2018

网格布局
@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QPushButton,QMessageBox,QDesktopWidget,
                             QGridLayout,QLabel,QLineEdit,QTextEdit)
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        grid=QGridLayout()
        grid.setSpacing(10) #设置组件的间距
        
        
        title=QLabel('Title')
        author=QPushButton('author')
        review=QLabel('Review')
        
        titleEdit = QLineEdit()
        authorEdit = QTextEdit()
        reviewEdit = QLineEdit()
        
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
 
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
 
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1,5,1)
       
               
        self.setLayout(grid)
        
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