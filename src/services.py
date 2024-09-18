from queries import CREATE_USER_TABLE,INSERT_USER
from sqlalchemy import text
from dbConnection import engine
class User:
    def __init__(self,name,email,phone_number,address,id=None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
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


def createUser(name,email,phone_number,address,file): 
    with engine.connect() as conn:
        conn.execute(text(CREATE_USER_TABLE))
        new_user = User(name,email,phone_number,address)
        file.write(f"new_user Object-->   {new_user}\n\n\n")
        conn.execute(text(INSERT_USER),[{"name":new_user.name,"email":new_user.email,"phone_number":new_user.phone_number,"address":new_user.address}])
        response = conn.execute(text(f"SELECT * FROM User where email = '{new_user.email}'")).all()
        file.write(f"select data value-->  {response[0]}\n\n\n")
        conn.commit()    
        return {"name":response[0][0],"email":response[0][1],"phone_number":response[0][2],"address":response[0][3],"id":response[0][4]}