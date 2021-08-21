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
    
    def checkTableNotExist(self, db_connection, tableName):
        """This method takes two argument mysql connection and table name to be check.
        If table exist in Database it returns true else false."""
        
        #creating cursor to execute query
        db_cursor = db_connection.cursor()
        
        #query to check if table exist
        checkTableQuery = "SELECT * FROM " + tableName
        try:
            db_cursor.execute(checkTableQuery)
            db_cursor.fetchall()
        except:
            db_cursor.close()
            return True

        db_cursor.close()
        return False
        
    def createTable(self, db_connection, tableName):
        """This method takes two argument mysql connection and table name to be check and creates table."""
        #create cusror to execute query
        db_cursor = db_connection.cursor()
        
        #query to create table
        createTableQuery = "CREATE TABLE " + tableName + "(CustomerName VARCHAR(255) NOT NULL,CustomerID VARCHAR(18) PRIMARY KEY, CustomerOpenDate DATE NOT NULL, LastConsultedDate DATE, VaccinatedType CHAR(5), DoctorConsulted CHAR(255), State CHAR(5), PostCode INT(5), DateOfBirth DATE, ActiveCustomer CHAR(1))"
        db_cursor.execute(createTableQuery)
        db_cursor.close()
    
    def insert(self, attributes):
        """This method takes list object as an argument."""
        
        #establishing connection with hospital database
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            port = "3306",
            database ="hospital",
            password = "5127990209")
        
        #checking if Table exist in Database or not
        if(self.checkTableNotExist(connection, attributes[7])):
            self.createTable(connection, attributes[7])
            
        #inserting data in the table
        db_cursor = connection.cursor()
        
        #query to insert data to table
        tableName = attributes.pop(7)
        
        #removing new line character
        temp = attributes.pop(9)
        attributes.append(temp[0])
        
        #formatting date of birth
        temp = attributes.pop(8)
        date = temp[0:2]
        month = temp[2:4]
        year = temp[4:8]
        temp = year + month + date
        attributes.insert(8, temp)
        
        #query to insert data
        insertQuery = "INSERT INTO " + tableName + " VALUES (\""+ attributes[0] +"\", "+ attributes[1] +", "+ attributes[2] +", "+ attributes[3] +", \""+ attributes[4] +"\", \""+ attributes[5] +"\", \""+ attributes[6] +"\", "+ attributes[7] +", "+ attributes[8] +", \""+ attributes[9] +"\")"
        db_cursor.execute(insertQuery)
        db_cursor.close()
        connection.commit()
        
    
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

        return counter
            
e1=Export("./../test.txt")
print(e1.toDataBase(), " rows inserted",)
