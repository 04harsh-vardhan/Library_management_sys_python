from http.server import SimpleHTTPRequestHandler
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Send response body (HTML content)
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")








    
