import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="nhandangkhuonmat"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM hocsinh")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
