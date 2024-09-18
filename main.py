from src.controller import MyHandler
from http.server import HTTPServer
import os

Logs = "Logs"
if not os.path.isdir(Logs):
    os.mkdir(Logs)

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
        
        