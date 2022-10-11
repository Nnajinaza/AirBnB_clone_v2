-- Creates a new database
-- Creates a new user in localhost and
-- Sets the password for the hbnb_test_db database
-- Sets User to have all priviledges on hbnb_test_db database
-- Sets User to have SELECT privilege on performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
