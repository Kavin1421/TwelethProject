-- SQL Script to create the schema with relationships
create database HosueRental;
use HosueRental;
-- Creating Signup Table
CREATE TABLE signup (
    idno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    emailid VARCHAR(100) UNIQUE NOT NULL,
    mobilenum VARCHAR(15) UNIQUE NOT NULL,
    category VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL 
);

-- Creating Owner Details Table
CREATE TABLE owner_details (
    ownerid INT AUTO_INCREMENT PRIMARY KEY,
    ownername VARCHAR(100) NOT NULL,
    ownerproof VARCHAR(255) NOT NULL,
    owneraddress TEXT NOT NULL,
    ownercontact VARCHAR(15) UNIQUE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    oemail VARCHAR(100) UNIQUE NOT NULL
);

-- Creating Booking Table
CREATE TABLE booking (
    bookingid INT AUTO_INCREMENT PRIMARY KEY,
    booking_date DATE NOT NULL,
    payment DECIMAL(10, 2) NOT NULL,
    paymentlastdate DATE NOT NULL,
    ownerid INT NOT NULL,
    paymentdone BOOLEAN DEFAULT FALSE,
    district VARCHAR(100) NOT NULL,
    FOREIGN KEY (ownerid) REFERENCES owner_details(ownerid) ON DELETE CASCADE
);

-- Creating Accommodation Details Table
CREATE TABLE accommodation_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL,
    college_name VARCHAR(100) NOT NULL,
    accounttype VARCHAR(50) NOT NULL,
    payment DECIMAL(10, 2) NOT NULL,
    ownerid INT NOT NULL,
    FOREIGN KEY (ownerid) REFERENCES owner_details(ownerid) ON DELETE CASCADE
);

-- Sample SELECT Queries

-- Retrieve all users from the signup table
SELECT * FROM signup;

-- Retrieve all bookings
SELECT * FROM booking;

-- Retrieve all owner details
SELECT * FROM owner_details;

-- Retrieve all accommodation details
SELECT * FROM accommodation_details;

commit;


-- Sample Insert Statements
-- 1. Inserting Data into owner_details
-- Here are some sample records for the owner_details table:
-- sql
INSERT INTO owner_details (ownername, ownerproof, owneraddress, ownercontact, amount, oemail) VALUES 
('John Doe', 'Passport', '123 Elm St, Springfield', '9876543210', 1000.00, 'john.doe@example.com'),
('Jane Smith', 'Driver License', '456 Oak St, Springfield', '8765432109', 1500.00, 'jane.smith@example.com'),
('Alice Johnson', 'Aadhar Card', '789 Pine St, Springfield', '7654321098', 1200.00, 'alice.johnson@example.com'),
('Bob Brown', 'Voter ID', '321 Maple St, Springfield', '6543210987', 900.00, 'bob.brown@example.com');
-- 2. Inserting Data into accommodation_details
-- Here are some sample records for the accommodation_details table:
-- sql
INSERT INTO accommodation_details (city_name, college_name, accounttype, payment, ownerid) VALUES 
('Springfield', 'Springfield University', 'Rent', 500.00, 1),  -- John Doe
('Springfield', 'Springfield College', 'Lease', 750.00, 2),   -- Jane Smith
('Shelbyville', 'Shelbyville Institute', 'Rent', 600.00, 3), -- Alice Johnson
('Capital City', 'Capital City University', 'Lease', 800.00, 4); -- Bob Brown