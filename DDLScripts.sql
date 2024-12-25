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
    category VARCHAR(50) NOT NULL
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