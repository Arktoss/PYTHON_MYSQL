import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database="ninja_turtles"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM turtles")
myresult = mycursor.fetchall()

print(mycursor)

for row in myresult:
    print(row)