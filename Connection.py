import mysql.connector

try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="1421@Kavin",  # Replace with your MySQL password
            database="HosueRental"  # Replace with your database name
        )
        print("Database connection successful.")
        print(conn)
       
except mysql.connector.Error as err:
        print(f"Error: {err}")
      
