from http.server import SimpleHTTPRequestHandler
import json

from jwt import InvalidSignatureError
from .services import createUser,loginUser,addMembership,addBooks
import os
from utils import createFile,sendResponse,extractJwtPayload,authFailed

if not os.path.isdir("Logs"):
    os.mkdir("Logs")

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Send response body (HTML content)
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")
    
    def do_POST(self):
        try:
            content_length = int(self.headers['content-Length'])
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))
            if not "auth" in self.path:
                jwt_token = self.headers['authorization']
                try:
                    extractJwtPayload(jwt_token)
                except InvalidSignatureError:
                    authFailed(self,{"error":"auth failed"})
            elif self.path == "/auth/signup":
                file = createFile("signup.txt")
                file.write(f"requested data -->  {json_data}\n\n\n")
                #services
                response = createUser(json_data['name'], json_data['email'], json_data['phone_number'], json_data['address'],json_data['password'],file)
                sendResponse(self,response,file)
            elif self.path == "/auth/login":
                file = createFile("login.txt")
                file.write(f"requested data -->  {json_data}\n\n\n")
                response = loginUser(json_data['email'],json_data['password'],file)
                sendResponse(self,response,file)
            elif self.path == "/addMember":
                file = createFile("addMember.txt")
                file.write(f"requested data -->  {json_data}\n\n\n")
                jwt_token = self.headers['authorization']
                file.write(f"jwt_token from payload -->  {jwt_token}\n\n\n")
                payload = extractJwtPayload(jwt_token)
                response = addMembership(payload['id'],json_data['membership_type'],file)
                sendResponse(self,response,file)
            elif self.path == "/addBooks":
                file = createFile("addBooks.txt")
                file.write(f"requested Data  -->  {json_data}\n\n\n")
                response = addBooks(json_data['books'])
                sendResponse(self,response,file)
        except json.JSONDecodeError:
                self.wfile.write("Data is not in correct Json format".encode('utf-8'))
                    
