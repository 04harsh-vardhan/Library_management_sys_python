from queries import CREATE_USER_TABLE,INSERT_USER,ADD_MEMBER,ADD_BOOKS
from sqlalchemy import text
from dbConnection import engine
import jwt


private_key = "help"
class User:
    def __init__(self,name,email,phone_number,address,password,id=None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.password = password
        self.user_id =  id
class Librarian(User):
    def __init__(self):
        pass

class Member(User):
    def __init__(self,user_id,membership_type,membership_start_date=None,membership_expiry_date=None):
        self.user_id = user_id
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
        conn.commit()  
        response = conn.execute(text(f"SELECT * FROM User where email = '{new_user.email}'")).all()
        file.write(f"Service query Response --> {response}\n\n\n")  
        return {"name":response[0][0],"email":response[0][1],"phone_number":response[0][2],"address":response[0][3],"id":response[0][5]}

def loginUser(email,password,file):
    with engine.connect() as conn:
        user = conn.execute(text(f"SELECT * FROM User WHERE email = '{email}' AND CAST(AES_DECRYPT(password,'key') AS CHAR) = '{password}'")).all()
        file.write(f"Service query result  --->  {user}\n\n\n")
        if len(user) > 0:
            jwt_payload = {
                "name":user[0][0],
                "email":user[0][1],
                "id":user[0][5]
            }
            token = jwt.encode(jwt_payload,private_key)
            return {"success":True, "token":token}
        else:
            return {"success":False,"msg":"incorrect email or Password"}

def addMembership(user_id,mem_type,file):
    with engine.connect() as conn:
        new_member= Member(user_id,mem_type).__dict__
        file.write(f"new_member  --->  {new_member}\n\n\n")
        check_query = conn.execute(text(f"Select Member.membership_type,  Member.membership_start_date,Member.membership_expiry_date,USER.name,USER.email from Member INNER JOIN USER ON Member.user_id = USER.user_id where Member.user_id = {user_id}")).all()
        if len(check_query):
            return {"status":"Already a member"}
        conn.execute(text(ADD_MEMBER),[new_member])
        conn.commit()
        query_response = conn.execute(text(f"Select Member.membership_type,  Member.membership_start_date,Member.membership_expiry_date,USER.name,USER.email from Member INNER JOIN USER ON Member.user_id = USER.user_id where Member.user_id = {user_id}")).all()
        file.write(f"Query Response --> {query_response}\n\n\n")
        return {"membership_type":query_response[0][0], "start_date":query_response[0][1],"expiry_date":query_response[0][2],"name":query_response[0][3],"email":query_response[0][4]}

def addBooks(books):
    try:
        with engine.connect() as conn:
            conn.execute(text(ADD_BOOKS),books)
            conn.commit()
            return {"success":"true","msg":"Data got Inserted Successfully"}
    except :
        {"success":"false", "msg":"My Sql Exception"}