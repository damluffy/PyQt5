# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:00:19 2019

@author: ai-pc
"""
import os

from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from Ui_bone_fracture_02 import Ui_Form

from PyQt5.QtCore import pyqtSignal,Qt

class MyMainWindow(QMainWindow,Ui_Form):
    

    helpSignal=pyqtSignal(str)
    printSignal=pyqtSignal(list)
    # 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([ int, str ], [ str ])
            
    def __init__(self,parent=None):
        
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        
        self.Filedic1=''   #所有病例的文件夹
        
        self.Filedic2=''   #某个病例的文件夹
        self.Filedic2_all=[]   #所有病例的文件夹列表
        self.current_num=0          #病例文件夹Filedic2在Filedic1里的序号，默认为0
        self.total_num=0           #Filedic1里病例的总数
        
        
        self.Filedic3=''   #某个病例某次检查的文件夹
        self.Filedic3_all=[] #某个病例所有检查的文件夹列表
        
        
    
    def initUi(self):
       
        self.pushButton.clicked.connect(self.openFiledic1)
        self.pushButton_2.clicked.connect(self.clearFiledic1)

        self.pushButton_3.clicked.connect(self.openFiledic2)        
        self.pushButton_4.clicked.connect(self.firstFiledic2)   #第一个病例
        self.pushButton_5.clicked.connect(self.formerFiledic2)  #前一个
        self.pushButton_6.clicked.connect(self.nextFiledic2)    #下一个
        self.pushButton_7.clicked.connect(self.lastFiledic2)    #最后一个
    
    def openFiledic1(self):
        
        self.Filedic1 = QFileDialog.getExistingDirectory(self,"选取文件夹", "./")
        self.lineEdit.setText(self.Filedic1)
        
        files = os.listdir(self.Filedic1)
        #print(files)
        for f in files:
            if(os.path.isdir(self.Filedic1 + '/' + f)):
                if(f[0] == '.'or f[0] =='$'):  # 排除隐藏文件夹。因为隐藏文件夹过多  
                    pass  
                else:  
                    self.Filedic2_all.append(f)   #不一定是按顺序的！！！！
        print(self.Filedic2_all) #打印测试
        self.total_num=len(self.Filedic2_all)
        
        self.Filedic2 = self.Filedic1 + '/' + self.Filedic2_all[0]  #初始化，默认为第一个病例的文件夹
        
    def clearFiledic1(self):
        
        self.lineEdit.clear()
        
    def openFiledic2(self):
        
        if self.Filedic1=='':
            QMessageBox.warning(self,"警告！",  "请先 选择文件夹！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.Filedic2 = QFileDialog.getExistingDirectory(self,"选取文件夹", self.Filedic1)       
        print(self.Filedic2) #打印测试
                
        current_Filedic2=self.Filedic2.replace(self.Filedic1+'/','')
        self.current_num=self.Filedic2_all.index(current_Filedic2)
                
        self.infoShow()
    
    def firstFiledic2(self):
        
        if self.Filedic1=='':
            QMessageBox.warning(self,"警告！",  "请先 选择文件夹！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.current_num=0
            
        self.Filedic2 = self.Filedic1 + '/' + self.Filedic2_all[self.current_num]       
        print(self.Filedic2) #打印测试     
        self.infoShow()
    
    def lastFiledic2(self):
        
        if self.Filedic1=='':
            QMessageBox.warning(self,"警告！",  "请先 选择文件夹！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.current_num=self.total_num-1
        
        self.Filedic2 = self.Filedic1 + '/' + self.Filedic2_all[self.current_num]       
        print(self.Filedic2) #打印测试
        self.infoShow()
    
    def formerFiledic2(self):
        if self.Filedic1=='':
            QMessageBox.warning(self,"警告！",  "请先 选择文件夹！", QMessageBox.Yes | QMessageBox.No)
        elif self.current_num!=0:
            self.current_num=self.current_num-1
        
        self.Filedic2 = self.Filedic1 + '/' + self.Filedic2_all[self.current_num]       
        print(self.Filedic2) #打印测试
    
        self.infoShow()
    
    
    def nextFiledic2(self):
        if self.Filedic1=='':
            QMessageBox.warning(self,"警告！",  "请先 选择文件夹！", QMessageBox.Yes | QMessageBox.No)
        elif self.current_num!=self.total_num-1:
            self.current_num=self.current_num+1
        
        self.Filedic2 = self.Filedic1 + '/' + self.Filedic2_all[self.current_num]       
        print(self.Filedic2) #打印测试
        
        self.infoShow()
    
    def infoShow(self):
        
        self.label_7.setText(str(self.current_num+1)+'/'+str(self.total_num))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    