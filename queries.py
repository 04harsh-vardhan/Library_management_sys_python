CREATE_USER_TABLE = "Create Table IF NOT EXISTS User(name VARCHAR(100),email VARCHAR(100), phone_number VARCHAR(32), address VARCHAR(100),user_id INT AUTO_INCREMENT PRIMARY KEY)"
INSERT_USER = "INSERT INTO User(name,email,phone_number,address) VALUES (:name,:email,:phone_number,:address)"
