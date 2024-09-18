from sqlalchemy import text
from dbConnection import engine
from queries import CREATE_USER_TABLE,INSERT_USER
from src.controller import MyHandler
from http.server import HTTPServer
class User:
    def __init__(self,name,email,phone_number,address):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

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


if __name__=="__main__":
    host = '127.0.0.1'
    port = 8081
    server = HTTPServer((host,port),MyHandler)
    try:
        print(f"server started at port {8081}")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print(f"server closed")
        
        