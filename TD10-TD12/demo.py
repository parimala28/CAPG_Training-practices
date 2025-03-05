import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pari@123 "
#   database="employee"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="pari@123",  # Replace with your actual MySQL password
#     database="employee",  # Replace with your database name
# )

# print("Connected to MySQL successfully!")
