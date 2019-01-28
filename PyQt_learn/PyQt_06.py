# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:40:09 2018
This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar, and a central widget.
@author: ai-pc
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QApplication,QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)
        
        exitAction=QAction(QIcon('F:/Py_learn/PyQt_learn/exit.jpg'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close) # exitAction.triggered.connect(qApp.quit)
        
        self.statusBar().showMessage('Ready')   #self.statusBar()
        
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        toolbar=self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
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
