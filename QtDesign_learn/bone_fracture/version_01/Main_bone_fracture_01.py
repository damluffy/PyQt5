# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:02:06 2019

@author: ai-pc
"""

from Link_bone_fracture_01 import MyMainWindow

class MyMain(MyMainWindow):
    def __init__(self,parent=None):
        super(MyMain, self).__init__(parent)

        

import sys
from PyQt5.QtWidgets import QApplication

if __name__=='__main__':
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())