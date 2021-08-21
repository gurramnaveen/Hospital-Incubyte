# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:04:18 2021

@author: nAVIN
"""

import mysql.connector

class Export:
    def __init__(self, filePath):
        self.fileObj = ""
        try:
            self.fileObj = open(filePath,"r")
        except:
            print("File Not Found!")
    
    def checkTableExist(self, db_connection, tableName):
        """This method takes two argument mysql connection and table name to be check.
        If table exist in Database it returns true else false."""
        
        #creating cursor to execute query
        db_cursor = db_connection.cursor()
        
        #query to check if table exist
        checkTableQuery = "SHOW TABLES LIKE " + tableName
        db_cursor.execute(checkTableQuery)
        
        if(db_cursor.fetchone()):
            return True
        else:
            return False
        
    def createTable(self, db_connection, tableName):
        """This method takes two argument mysql connection and table name to be check and creates table."""
        #create cusror to execute query
        db_cursor = db_connection.cursor()
        
        #query to create table
        createTableQuery = "CREATE TABLE " + tableName + "(CustomerName VARCHAR(255) NOT NULL,CustomerID VARCHAR(18) PRIMARY KEY,	CustomerOpenDate DATE NOT NULL,	LastConsultedDate DATE,	VaccinatedType CHAR(5),	DoctorConsulted CHAR(255),	State CHAR(5), PostCode INT(5), DateOfBirth DATE, ActiveCustomer CHAR(1))"
        db_cursor.execute(createTableQuery)
    
    def insert(self, attributes):
        """This method takes list object as an argument."""
        
        #establishing connection with hospital database
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            port = "3306",
            database ="hospital")
        
        #checking if Table exist in Database or not
        if not self.checkTableExist(connection, attributes[7]):
            self.createTable(connection, attributes[7])
            
        #inserting data in the table
        db_cursor = connection.cursor()
        
        #query to insert data to table
        tableName = attributes.pop(7)
        insertQuery = "INSERT INTO " + tableName + " VALUES (%s, %s, %s, %s, %s, %s, %s, %d, %s, %s)"
        db_cursor.execute(insertQuery, attributes)
        
    
    def toDataBase(self):
        """This method doesn't take any argument.
        But returns number of rows inserted.
        It's purpose is to insert the data to database"""
        
        counter = 0
        #returns if file Object is null
        if(self.fileObj == ""): return
        
        #reading data row by row and inserting in database
        for line in self.fileObj:
            
            #converting pipe delimeted row to list
            dataList=line.split('|')
            dataList.pop(0)
            if(dataList[0] == 'D'):
                
                #removing metadata showing Details Record Layout
                dataList.pop(0)
                self.insert(dataList)
                counter += 1
            
e1=Export("./../test.txt")
e1.toDataBase()