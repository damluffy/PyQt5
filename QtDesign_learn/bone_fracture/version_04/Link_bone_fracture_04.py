# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:00:19 2019

@author: ai-pc
"""
import os

from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from Ui_bone_fracture_04 import Ui_Form

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
        self.current_num=0          #某个病例的文件夹Filedic2在Filedic1里的序号，默认为0
        self.total_num=0           #Filedic1里病例的总数
        
        
        self.Filedic3=''     #某个病例某次检查的文件夹
        self.Filedic3_all=[] #某个病例所有检查的文件夹列表
        self.current_num_1=0 #某次检查的序号
        self.total_num_1=0   #所有检查的总数
        
        
    
    def initUi(self):
       
        self.pushButton.clicked.connect(self.openFiledic1)
        self.pushButton_2.clicked.connect(self.clearFiledic1)

        self.pushButton_3.clicked.connect(self.openFiledic2)        
        self.pushButton_4.clicked.connect(self.firstFiledic2)   #第一个病例
        self.pushButton_5.clicked.connect(self.formerFiledic2)  #前一个
        self.pushButton_6.clicked.connect(self.nextFiledic2)    #下一个
        self.pushButton_7.clicked.connect(self.lastFiledic2)    #最后一个
    
    def openFiledic1(self):
        
        self.Filedic1 = QFileDialog.getExistingDirectory(self,"选取文件夹", "/home")
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
            
        self.Filedic3_all=[]
        
        files2 = os.listdir(self.Filedic2)        
        
        for f in files2:
            if(os.path.isdir(self.Filedic2 + '/' + f)):
                if(f[0] == '.'or f[0] =='$'):  # 排除隐藏文件夹。因为隐藏文件夹过多  
                    pass  
                else:  
                    self.Filedic3_all.append(f)   #不一定是按顺序的！！！！
        print(self.Filedic3_all) #打印测试
        self.total_num_1=len(self.Filedic3_all)
        
        self.Filedic3 = self.Filedic2 + '/' + self.Filedic3_all[0]  #初始化，默认为第一次检查的文件夹
        print(self.Filedic3)
        
        self.showLineEdit_2_6()            #lineEdit2~6的设定
        
        self.label_8.setText(str(1)+'/'+str(self.total_num_1))   #初始化
        
        self.showText()
        
        self.showImage()   #默认显示第一张图
    
    def showLineEdit_2_6(self):
        
        x=self.Filedic2_all[self.current_num]
        y=x.split('_')
        print(y)
        
        age=y[1]
        sex=y[2]
        which=y[3]
        self.lineEdit_2.setText(sex)
        self.lineEdit_3.setText(age)
        self.lineEdit_4.setText(which)
        
        x1=self.Filedic3_all[0]
        y1=x1.split(' ')
        print(y1)
        if (len(y1)>1):
            if y1[1]=='无异常':
                self.lineEdit_6.setText('否')
            else:
                self.lineEdit_6.setText('是')
        else:
                self.lineEdit_6.setText('是')                   #显示第一次检查的骨折状态
                
        self.lineEdit_5.setText(y1[0][-10:])                    #默认显示第一次检查的日期
    
    def showText(self):
        
        files3 = os.listdir(self.Filedic3)
        text_path=''
        
        for f3 in files3:
            if f3.endswith('.txt'):
                text_path=self.Filedic3 + '/' + f3
        
        if text_path=='':
            self.textEdit.setText('首次检查 即为 复查')
        else:
            f_txt=open(text_path,'r')
            with f_txt:
                data=f_txt.read()
                self.textEdit.setText(data) 
                
            
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    