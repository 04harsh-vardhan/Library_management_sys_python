CREATE_USER_TABLE = "Create Table IF NOT EXISTS User(name VARCHAR(100),email VARCHAR(100), phone_number VARCHAR(32), address VARCHAR(100),password BLOB,user_id INT AUTO_INCREMENT PRIMARY KEY)"
INSERT_USER = "INSERT INTO User(name,email,phone_number,address,password) VALUES (:name,:email,:phone_number,:address,:password)"
ADD_MEMBER = "INSERT INTO MEMBER(user_id,membership_type,membership_start_date,membership_expiry_date) VALUES (:user_id,:membership_type,:membership_start_date,:membership_expiry_date)"
ADD_BOOKS = "INSERT INTO BOOKS (author,title,edition) VALUES (:author,:title,:edition)"