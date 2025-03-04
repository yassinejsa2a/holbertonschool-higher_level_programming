-- This SQL script creates a table named 'second_table' if it does not already exist and inserts four rows of data into it.
CREATE TABLE IF NOT EXISTS second_table (id INT,name VARCHAR(256),score INT);
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
