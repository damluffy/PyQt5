# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:55:01 2019

@author: ai-pc
"""

from PyQt5.QtWidgets import QMainWindow
from print_test_Ui import Ui_Form
from PyQt5.QtCore import pyqtSignal,Qt

class MyMainWindow(QMainWindow,Ui_Form):
    
    helpSignal=pyqtSignal(str)
    printSignal=pyqtSignal(list)
    # 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([ int, str ], [ str ])
            
    def __init__(self,parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int,str].connect(self.previewPaperWithArgs)
        
        self.pushButton_2.clicked.connect(self.emitPrintSignal)
        self.pushButton.clicked.connect(self.emitPreviewSignal)

    def emitPreviewSignal(self):
        if self.checkBox.isChecked()==True:
            self.previewSignal[int,str].emit(1080,'Full Screen')
        elif self.checkBox.isChecked()==False:
            self.previewSignal[str].emit('Preview')
    
    def emitPrintSignal(self):
        pList=[]
        pList.append(self.spinBox.value())
        pList.append(self.comboBox.currentText())
        self.printSignal.emit(pList)
    
    def printPaper( self, list ):
        self.textEdit.setText("打印: " + "份数：" + str(list[ 0 ]) + " 纸张：" + str(list[ 1 ]))
    
    def previewPaperWithArgs( self, style, text ):
        self.textEdit.setText(str(style) + text)
    
    def previewPaper( self, text ):
        self.textEdit.setText(text)

    def keyPressEvent( self, event ):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")
    
    def showHelpMessage( self, message ):
        self.textEdit.setText(message)
        self.statusBar().showMessage(message)
     

