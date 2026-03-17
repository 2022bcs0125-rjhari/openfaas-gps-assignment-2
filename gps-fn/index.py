from function.handler import handle
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        result = handle("")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(result.encode())

    def do_POST(self):   # ✅ ADD THIS
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        result = handle(body)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(result.encode())

def run():
    server = HTTPServer(('0.0.0.0', 5000), Handler)
    server.serve_forever()

if __name__ == "__main__":
    run()