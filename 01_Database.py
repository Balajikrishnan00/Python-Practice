# Tutorial
""""
import mysql.connector

mydatase=mysql.connector.connect(host='localhost',user='root',password='root')

print(mydatase)
"""
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root')
newDatabase='CREATE DATABASE HELLODB;'
#db=tuple(input('Enter db name:'))
cusr=con.cursor()
cusr.execute(newDatabase)
print('Database created successfully')

