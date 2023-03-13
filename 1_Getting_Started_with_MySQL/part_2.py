import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database="ninja_turtles"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE ninja_turtles")
#mycursor.execute("SHOW DATABASES")
#
#for db in mycursor:
#    print(db)
#

#mycursor.execute(f"CREATE TABLE turtles (name Varchar(255), color VARCHAR(255), weapon VARCHAR(255), pizza BOOLEAN, age INT(3))")\

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)