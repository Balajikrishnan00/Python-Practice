# Tutorial
""""
import mysql.connector

mydatase=mysql.connector.connect(host='localhost',user='root',password='root')

print(mydatase)

import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root')
newDatabase='CREATE DATABASE HELLODB;'
#db=tuple(input('Enter db name:'))
cusr=con.cursor()
cusr.execute(newDatabase)
print('Database created successfully')
"""
import mysql.connector
def NewDatabase(dbname):
    connection=mysql.connector.connect(host='localhost',user='root',password='root')
    cusr=connection.cursor()
    cusr.execute(f'CREATE DATABASE {dbname};')
    connection.commit()
    print('database create successfully.')

def DeleteDatabase(dbname):
    connection = mysql.connector.connect(host='localhost', user='root', password='root')
    crsr=connection.cursor()
    crsr.execute(f'DROP DATABASE {dbname};')
    connection.commit()
    print('database delete successfully.')



dbname=input('Enter DB name:')
#NewDatabase(dbname)
DeleteDatabase(dbname)
