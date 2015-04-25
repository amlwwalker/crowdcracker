from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Just received a GET request")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        imsi = query_components["imsi"]
        self.wfile.write('Hello world ' + str(imsi))

        return

    def log_request(self, code=None, size=None):
        print('Request')

    def log_message(self, format, *args):
        print('Message')

if __name__ == "__main__":
    try:
        server = HTTPServer(('localhost', 80), MyHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()