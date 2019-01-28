# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:50:08 2018

@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif',10))   #设置10号大小的SansSerif字体        
        self.setToolTip('This is a <b>QWidget</b> widget')   #设置窗口的提示文字
        
        btn=QPushButton('Click me',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') #设置button的提示文字
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        
        qbtn=QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit) #点一下退出
        qbtn.setToolTip('This is a <b>QPushButton</b> quit widget') #设置button的提示文字
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150,150)
        
        
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Click and close')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg'))       
        
        self.show()
        
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






