from http.server import SimpleHTTPRequestHandler
import json
from .services import createUser
import os
from utils import createFileIfNotExists,sendResponse

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Send response body (HTML content)
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")
    
    def do_POST(self):
        content_length = int(self.headers['content-Length'])
        post_data = self.rfile.read(content_length)
        if self.path == "/signup":
            Logs = "Logs/signup"
            if not os.path.isdir(Logs):
                os.mkdir(Logs)
            file = createFileIfNotExists(Logs)
            try:
                json_data = json.loads(post_data.decode('utf-8'))
                file.write(f"Request Payload-->   {json_data}\n\n\n")
                response = createUser(json_data['name'], json_data['email'], json_data['phone_number'], json_data['address'],file)
                json_response = json.dumps(response)
                file.write(f"json_response-->    {json_response}\n\n\n")
                sendResponse(response,self,file)
            except json.JSONDecodeError:
                self.wfile.write("Some exception has occured".encode('utf-8'))
            
