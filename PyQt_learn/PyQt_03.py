# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:34:13 2018

@author: ai-pc
"""


import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QIcon,QFont

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
        
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Click')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg'))
    
        
        
        self.show()
        

if __name__=='__main__':
    
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
