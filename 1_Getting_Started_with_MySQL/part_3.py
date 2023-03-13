import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database="ninja_turtles"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO turtles (name, color, weapon, pizza, age) VALUES (%s, %s, %s, %s, %s)"

#leonardo = ("Leonardo", "Blue", "Katana", True, 15)
turtles = [("Raphael", "Red", "Sai", True, 15),
           ("Donatello", "Purple", "Bo", True, 15),
           ("Michelangelo", "Orange", "Nunchucks", True, 15)]

#mycursor.execute(sqlFormula, leonardo)
mycursor.executemany(sqlFormula, turtles)

mydb.commit()