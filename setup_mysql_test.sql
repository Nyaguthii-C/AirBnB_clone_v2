-- Creates a database  hbnb_dev_db 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants Permissions for  hbnb_test
GRANT ALL ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
