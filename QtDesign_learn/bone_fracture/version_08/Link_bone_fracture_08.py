# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:00:19 2019

@author: ai-pc
"""
import os

from PyQt5.QtWidgets import (QMainWindow,QFileDialog,QMessageBox,
                            QGraphicsScene, QGraphicsPixmapItem)
from Ui_bone_fracture_02 import Ui_Form

from PyQt5.QtCore import pyqtSignal,Qt,QSize

from PyQt5.QtGui import QPixmap,QImage

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
        
        self.image_path=''  #图片jpg路径
        self.image_path_all=[] #图片列表
        self.current_num_2=0 #某张图片序号
        self.total_num_2=0  #所有图片总数
        
        
    
    def initUi(self):
       
        self.pushButton.clicked.connect(self.openFiledic1)
        self.pushButton_2.clicked.connect(self.clearFiledic1)

        self.pushButton_3.clicked.connect(self.openFiledic2)        
        self.pushButton_4.clicked.connect(self.firstFiledic2)   #第一个病例
        self.pushButton_5.clicked.connect(self.formerFiledic2)  #前一个
        self.pushButton_6.clicked.connect(self.nextFiledic2)    #下一个
        self.pushButton_7.clicked.connect(self.lastFiledic2)    #最后一个
        
        self.pushButton_10.clicked.connect(self.openFiledic3)        
        self.pushButton_12.clicked.connect(self.firstFiledic3)   #第一次检查
        self.pushButton_8.clicked.connect(self.formerFiledic3)  #前一次
        self.pushButton_11.clicked.connect(self.nextFiledic3)    #下一次
        self.pushButton_9.clicked.connect(self.lastFiledic3)    #最后一次
        
        self.pushButton_15.clicked.connect(self.firstImage)   #第一张图片
        self.pushButton_21.clicked.connect(self.formerImage)  #前一张
        self.pushButton_22.clicked.connect(self.nextImage)    #下一张
        self.pushButton_16.clicked.connect(self.lastImage) 
        
        self.comboBox.currentTextChanged.connect(self.updateLineEdit_7)
        self.comboBox_2.currentTextChanged.connect(self.updateLineEdit_7)
        self.comboBox_3.currentTextChanged.connect(self.updateLineEdit_7)
    
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
        
        #self.Filedic2 = self.Filedic1 + '/' + self.Filedic2_all[0]  #初始化，默认为第一个病例的文件夹
        
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
        
        self.current_num_1=0  
        self.Filedic3 = self.Filedic2 + '/' + self.Filedic3_all[self.current_num_1]  #初始化，默认为第一次检查的文件夹
        print(self.Filedic3)
        
        self.showLineEdit_2_6()            #lineEdit2~6的设定
        self.lineEdit_7.setText('')
               
        self.label_8.setText(str(1)+'/'+str(self.total_num_1))   #初始化
        
        self.showText()
        
        self.current_num_2=0
        self.image_path_all=[]
        files4 = os.listdir(self.Filedic3)
        print(files4)
        for f4 in files4:
            if (f4.endswith('.jpg') or f4.endswith('.JPG')):
                self.image_path_all.append(f4)
        print(self.image_path_all)
        self.total_num_2=len(self.image_path_all)
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
        
                
    def openFiledic3(self):
        
        if self.Filedic2=='':
            QMessageBox.warning(self,"警告！",  "请先 选择病例！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.Filedic3 = QFileDialog.getExistingDirectory(self,"选取文件夹", self.Filedic2)       
        print(self.Filedic3) #打印测试
                
        current_Filedic3=self.Filedic3.replace(self.Filedic2+'/','')
        self.current_num_1=self.Filedic3_all.index(current_Filedic3)
                
        self.infoShow2()
    
    def firstFiledic3(self):
        
        if self.Filedic2=='':
            QMessageBox.warning(self,"警告！",  "请先 选择病例！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.current_num_1=0
            
        self.Filedic3 = self.Filedic2 + '/' + self.Filedic3_all[self.current_num_1]       
        print(self.Filedic3) #打印测试     
        self.infoShow2()
    
    def lastFiledic3(self):
        
        if self.Filedic2=='':
            QMessageBox.warning(self,"警告！",  "请先 选择病例！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.current_num_1=self.total_num_1-1
        
        self.Filedic3 = self.Filedic2 + '/' + self.Filedic3_all[self.current_num_1] 
        print(self.Filedic3) #打印测试
        self.infoShow2()
    
    def formerFiledic3(self):
        if self.Filedic2=='':
            QMessageBox.warning(self,"警告！",  "请先 选择病例！", QMessageBox.Yes | QMessageBox.No)
        elif self.current_num_1!=0:
            self.current_num_1=self.current_num_1-1
        
        self.Filedic3 = self.Filedic2 + '/' + self.Filedic3_all[self.current_num_1]       
        print(self.Filedic3) #打印测试
    
        self.infoShow2()
    
    
    def nextFiledic3(self):
        if self.Filedic2=='':
            QMessageBox.warning(self,"警告！",  "请先 选择病例！", QMessageBox.Yes | QMessageBox.No)
        elif self.current_num_1!=self.total_num_1-1:
            self.current_num_1=self.current_num_1+1
        
        self.Filedic3 = self.Filedic2 + '/' + self.Filedic3_all[self.current_num_1]       
        print(self.Filedic3) #打印测试
        
        self.infoShow2()  
    
    def infoShow2(self):
        self.label_8.setText(str(self.current_num_1+1)+'/'+str(self.total_num_1))
        
        self.showLineEdit_5()
        
        self.current_num_2=0
        self.image_path_all=[]
        files4 = os.listdir(self.Filedic3)
        print(files4)
        for f4 in files4:
            if (f4.endswith('.jpg') or f4.endswith('.JPG')):
                self.image_path_all.append(f4)
        print(self.image_path_all)
        
        self.total_num_2=len(self.image_path_all)
        print(self.total_num_2)
       
        self.showImage()   #默认显示第一张图
        
        
    def showLineEdit_5(self):
        x2=self.Filedic3_all[self.current_num_1]
        y2=x2.split(' ')
        self.lineEdit_5.setText(y2[0][-10:])  
    
    def showImage(self):                       #显示第一次检查的第一张图片
        
        self.label_16.setText(str(self.current_num_2+1)+'/'+str(self.total_num_2))
               
        self.image_path=self.Filedic3 + '/' + self.image_path_all[self.current_num_2]
        
        img=QImage(self.image_path)
        size=QSize(650,690)
        pixImg = QPixmap.fromImage(img.scaled(size, Qt.KeepAspectRatio))
        
        self.graphicsView.scene = QGraphicsScene()            # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(pixImg)                # 创建一个变量用于承载加载后的图片
        self.graphicsView.scene.addItem(item)                 # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)   # 这个我也不知道是做了个啥
        
    def firstImage(self):
        
        if self.Filedic3=='':
            QMessageBox.warning(self,"警告！",  "请先 选择检查次数！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.current_num_2=0
              
        self.showImage()
    
    def lastImage(self):
        
        if self.Filedic3=='':
            QMessageBox.warning(self,"警告！",  "请先 选择检查次数！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.current_num_2=self.total_num_2-1
        
        self.showImage()
    
    def formerImage(self):
        if self.Filedic3=='':
            QMessageBox.warning(self,"警告！",  "请先 选择检查次数！", QMessageBox.Yes | QMessageBox.No)
        elif self.current_num_2!=0:
            self.current_num_2=self.current_num_2-1
        
        self.showImage()
    
    
    def nextImage(self):
        if self.Filedic3=='':
            QMessageBox.warning(self,"警告！",  "请先 选择检查次数！", QMessageBox.Yes | QMessageBox.No)
        elif self.current_num_2!=self.total_num_2-1:
            self.current_num_2=self.current_num_2+1
        
        self.showImage()      
        
    def updateLineEdit_7(self):
        
        if self.lineEdit_6.text()=='是':
            str1=self.comboBox.currentText()
            str2=self.comboBox_2.currentText()
            str3=self.comboBox_3.currentText() 
            self.lineEdit_7.setText(str1+str(float(str2)+float(str3)))    
        else:
            self.lineEdit_7.setText('无异常')
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    