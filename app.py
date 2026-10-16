from http.server import BaseHTTPRequestHandler, HTTPServer

def get_message():
    return "Hello from the DevOps pipeline!"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = get_message().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
