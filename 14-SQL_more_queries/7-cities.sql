-- Task 7:
-- creates the database hbtn_0d_usa and the table cities (in the database
-- hbtn_0d_usa) on your MySQL server

-- Creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates the table in the created database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL);