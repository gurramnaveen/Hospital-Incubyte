# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:04:18 2021

@author: nAVIN
"""

class Export:
    def __init__(self, filePath):
        self.fileObj = ""
        try:
            self.fileObj = open(filePath,"r")
        except:
            print("File Not Found!")
    
    def toDataBase(self):
        if(self.fileObj == ""): return
        for line in self.fileObj:
            dataList=line.split('|')
            dataList.pop(0)
            if(dataList[0] == 'D'):
                print(dataList)
            
e1=Export("./../test.txt")
e1.toDataBase()