import mysql.connector
from getpass import getpass
import random
import bcrypt

# MySQL connection setup
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="1421@Kavin",  # Replace with your MySQL password
            database="HosueRental"  # Replace with your database name
        )
        print("Database connection successful.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Signup function to add users to the signup table
def signup():
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    emailid = input("Enter your email id: ")
    mobilenum = input("Enter your mobile number: ")
    category = input("Enter your category (e.g., student, owner): ")
    password = getpass("Create a password: ")  # Get password securely

    # Hash the password for secure storage
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    print("Attempting to sign up...")
    
    # Get DB connection
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return
    
    cursor = conn.cursor()
    
    try:
        # Insert new user into signup table
        cursor.execute("""
            INSERT INTO signup (name, dob, emailid, mobilenum, category, password) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, dob, emailid, mobilenum, category, hashed_password))
        
        conn.commit()
        print("Signup successful!")
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        conn.rollback()  # Rollback in case of error
        
    finally:
        cursor.close()
        conn.close()

# Login function to authenticate users
def login():
    emailid = input("Enter your email id: ")
    password = getpass("Enter your password: ")
    
    # Get DB connection
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return None
    
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM signup WHERE emailid = %s", (emailid,))
        user = cursor.fetchone()
        
        if user:
            # Check if the provided password matches the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'), user[5].encode('utf-8')):  # Assuming password is at index 5
                print("Login successful!")
                return user
            else:
                print("Invalid email or password!")
                return None
        else:
            print("Invalid email or password!")
            return None
            
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None
        
    finally:
        cursor.close()
        conn.close()

# Function to display available accommodations and book one
def book_accommodation(user_id):
    print("Available Accommodations:")
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT a.id, a.city_name, a.college_name, a.accounttype, a.payment, o.ownername
            FROM accommodation_details a
            JOIN owner_details o ON a.ownerid = o.ownerid
        """)
        
        accommodations = cursor.fetchall()
        
        if not accommodations:
            print("No accommodations available at the moment.")
            return
        
        for idx, ac in enumerate(accommodations):
            print(f"{idx + 1}. City: {ac[1]}, College: {ac[2]}, Type: {ac[3]}, Price: {ac[4]}, Owner: {ac[5]}")
        
        choice = int(input("\nSelect an accommodation to book (1-{}): ".format(len(accommodations))))
        selected_accommodation = accommodations[choice - 1]
        
        # Insert booking into the booking table
        booking_id = random.randint(1000, 9999)  # Generate a random booking ID
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        payment = selected_accommodation[4]
        paymentlastdate = input("Enter payment last date (YYYY-MM-DD): ")

        cursor.execute("""
            INSERT INTO booking (bookingid, booking_date, payment, paymentlastdate, ownerid, paymentdone, district)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (booking_id, booking_date, payment, paymentlastdate, selected_accommodation[0], False, selected_accommodation[1]))
        
        conn.commit()

        print("Accommodation booked successfully!")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        
    finally:
        cursor.close()
        conn.close()

# Main program function to interact with the user
def main():
    print("Welcome to House Booking System!")
    
    while True:
        try:
            print("\n1. Signup")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                signup()
            elif choice == "2":
                user = login()
                if user:
                    print("\nBooking Options:")
                    book_accommodation(user[0])
            elif choice == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
