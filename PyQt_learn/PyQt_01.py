# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:21:24 2018

使用PyQt5创建一个简单的窗口
@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    
    app=QApplication(sys.argv)
    
    w=QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('First Trail')
    w.show()
    
    sys.exit(app.exec_())
    