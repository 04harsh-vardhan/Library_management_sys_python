import os

def createFileIfNotExists(file_path):
    file = open('logs.txt','a')
    return file

def sendResponse(response,obj,file):
    file.close()
    obj.send_response(200)
    obj.send_header('content-type','application/json')
    obj.end_headers()
    obj.wfile.write(response.encode('utf-8'))