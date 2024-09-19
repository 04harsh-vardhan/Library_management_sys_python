from queries import CREATE_USER_TABLE,INSERT_USER
from sqlalchemy import text
from dbConnection import engine
import jwt
class User:
    def __init__(self,name,email,phone_number,address,password,id=None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.password = password
        self.id = id
class Librarian(User):
    def __init__(self):
        pass

class Member(User):
    def __init__(self,membership_type,membership_start_date,membership_expiry_date):
        self.membership_type= membership_type
        self.membership_start_date=membership_start_date
        self.membership_expiry_date=membership_expiry_date


class Book:
    def __init__(self,title,author,edition):
        self.title = title
        self.author = author
        self.edition = edition

class Library:
    def __init__(self):
        pass


def createUser(name,email,phone_number,address,password,file): 
    with engine.connect() as conn:
        conn.execute(text(CREATE_USER_TABLE))
        new_user = User(name,email,phone_number,address,password)
        file.write(f"new_user -->   {new_user}\n\n\n")
        conn.execute(text(INSERT_USER),[new_user.__dict__])
        response = conn.execute(text(f"SELECT * FROM User where email = '{new_user.email}'")).all()
        file.write(f"Service query Response --> {response}\n\n\n")
        conn.commit()    
        return {"name":response[0][0],"email":response[0][1],"phone_number":response[0][2],"address":response[0][3],"id":response[0][5]}

def loginUser(email,password,file):
    with engine.connect() as conn:
        user = conn.execute(text(f"SELECT * FROM User WHERE email = '{email}' AND password = '{password}'")).all()
        file.write(f"Service query result  --->  {user}\n\n\n")
        if len(user) > 0:
            jwt_payload = {
                "name":user[0][0],
                "email":user[0][1]
            }
            private_key = "help"
            token = jwt.encode(jwt_payload,private_key)
            return {"success":True, "token":token}
        else:
            return {"success":False,"msg":"incorrect email or Password"}