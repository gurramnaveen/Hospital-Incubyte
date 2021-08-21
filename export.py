# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:04:18 2021

@author: nAVIN
"""

import mysql.connector
connection = mysql.connector.connect(
    host = "localhost"
    user = "root"
    port = "3306"
    database ="hospital")

class Export:
    def __init__(self, filePath):
        self.fileObj = ""
        try:
            self.fileObj = open(filePath,"r")
        except:
            print("File Not Found!")
    
    def insert(self, attributes):
        self.checkTableExist()
        
    
    def toDataBase(self):
        """This method doesn't take any argument.
        But returns number of rows inserted.
        It's purpose is to insert the data to database"""
        if(self.fileObj == ""): return
        for line in self.fileObj:
            dataList=line.split('|')
            dataList.pop(0)
            if(dataList[0] == 'D'):
                dataList.pop(0)
                self.insert(dataList)
            
e1=Export("./../test.txt")
e1.toDataBase()