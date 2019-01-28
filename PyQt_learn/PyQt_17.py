# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:29:48 2018

文件对话框

单个文件打开 QFileDialog.getOpenFileName()
多个文件打开 QFileDialog.getOpenFileNames()

文件夹选取     QFileDialog.getExistingDirectory()

文件保存         QFileDialog.getSaveFileName()
--------------------- 
作者：翻滚吧挨踢男 
来源：CSDN 
原文：https://blog.csdn.net/a359680405/article/details/45166271 
版权声明：本文为博主原创文章，转载请附上博文链接！


@author: ai-pc
"""

import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QMessageBox,QDesktopWidget,
                             QTextEdit,QAction,QFileDialog)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.textEdit=QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar
        
        openFile=QAction(QIcon('open.jpg'),'Open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)  
        
        menuBar=self.menuBar()
        fileMenu=menuBar.addMenu('&File')
        fileMenu.addAction(openFile)
        
        
        self.resize(300,220)
        self.center()   #设置居中
        
        self.setWindowTitle('Color Dialog')
        self.setWindowIcon(QIcon('F:/Py_learn/PyQt_learn/bone.jpg')) 
        
        self.show()
    
    def showDialog(self):
        
        fname=QFileDialog.getOpenFileName(self,'Open File','/home')
        print(fname)
        if fname[0]:
            f=open(fname[0],'r')
            with f:
                data=f.read()
                print(data)
                self.textEdit.setText(data)        
    
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