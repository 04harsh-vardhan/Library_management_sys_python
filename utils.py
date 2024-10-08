import os
import json
import jwt

def createFile(file_name):
    folder_path = "Logs"
    file_path = os.path.join(folder_path,file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    file = open(file_path,'a')
    return file
    

def sendResponse(obj,response,file):
    json_response = json.dumps(response)
    file.write(f"response -->  {json_response}\n\n\n")
    obj.send_response(200)
    obj.send_header('content-type','application/json')
    obj.end_headers()
    obj.wfile.write(json_response.encode('utf-8'))
    file.close()

def authFailed(obj,response):
    json_response = json.dumps(response)
    obj.send_response(401)
    obj.end_headers()
    obj.wfile.write(json_response.encode('utf-8'))

def extractJwtPayload(token):
    try:
        token = jwt.decode(token,"help",algorithms=['HS256', ])
        return token
    except:
        raise jwt.InvalidSignatureError