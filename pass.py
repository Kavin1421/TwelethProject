# import bcrypt

# # Example password
# password = "$2b$12$EixZaYVKc8g5nG2gR0lD8uW3m6e7O5H9Qq8D9zF5qIuA0d9/1cP7i"

# # Hashing the password
# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# print(hashed_password.decode('utf-8'))  # Print the hashed password as a string

import bcrypt

# Example user input
input_password = "$2b$12$EixZaYVKc8g5nG2gR0lD8uW3m6e7O5H9Qq8D9zF5qIuA0d9/1cP7i"  # Replace with actual user input

# Retrieve the stored hash from the database
stored_hash = '$2b$12$3wXcgg4GMjXyQkV1dzBH3.S9eAKfqww9UKvb8H/ETJPtYfOIwBCjG'  # Example hash

# Check if the entered password matches the stored hash
if bcrypt.checkpw(input_password.encode('utf-8'), stored_hash.encode('utf-8')):
    print("Password is correct!")
else:
    print("Invalid password.")
