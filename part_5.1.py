import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database="ninja_turtles"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO turtles (name, color, weapon, pizza, age) VALUES (%s, %s, %s, %s, %s)"

#leonardo = ("Leonardo", "Blue", "Katana", False, 15)
turtles = [("Raphael", "Red", "Sai", False, 19),
           ("Donatello", "Purple", "Bo", False, 17),
           ("Michelangelo", "Orange", "Nunchucks", False, 18)
           ("Bob", "Green", "Si", False, 19),
           ("Michelle", "Nurple", "Ko", False, 17),
           ("Michele", "Brown", "Nunnery", False, 19),
           ("Tommy two tone", "Green", "Scion", False, 19),
           ("Jenni", "Nurple", "Low Staff", False, 17),
           ("Sho Nuff", "Brown", "Chuck Norris", False, 8),
           ("Bruce Lee Roy Green", "Brown", "Spong bob", False, 29),]

#mycursor.execute(sqlFormula, leonardo)
mycursor.executemany(sqlFormula, turtles)

mydb.commit()