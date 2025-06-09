-- Create and populate the amdb database for testing
CREATE DATABASE IF NOT EXISTS amoldb;
USE amoldb;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
INSERT INTO users (name, age) VALUES
    ('Alice', 35),
    ('Bob', 50);

-- Products table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);
INSERT INTO products (name, price) VALUES
    ('Book', 25.99),
    ('Pen', 85.00);

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer VARCHAR(255)
);
INSERT INTO orders (customer) VALUES
    ('Alice'),
    ('Bob');
