import mysql.connector
"""
def TableCreate(dbname):
    connection=mysql.connector.connect(host='localhost',user='root',password='root',database=dbname)
    crsr=connection.cursor()
    crsr.execute('CREATE TABLE USER1(ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(255));')

    connection.close()
    print('Table created.')

dbname=input('Enter dbname:')
TableCreate(dbname)
------------------------------------------------------"""
def createTable(dbname):
    connection=mysql.connector.connect(host='localhost',user='root',password='root',database=dbname)
    crsr=connection.cursor()
    #taname=input('Enter table name:')
    sql='CREATE TABLE s(id int not null auto_increment primary key,name varchar(255);'
    crsr.execute(sql)
    print('table created successfully')

dbname=input('Enter DB name:')
createTable(dbname)