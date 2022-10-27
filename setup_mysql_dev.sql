-- Creates a new database
-- Creates a new user in localhost and
-- Sets the password for the hbnb_dev_db database
-- Sets User to have all priviledges on hbnb_dev_db database
-- Sets User to have SELECT privilege on performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
