import http.server
import socketserver
import json
from http import HTTPStatus


class Handler(http.server.BaseHTTPRequestHandler):
    _events = []
    def do_GET(self):
        if self.path == "/hello":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        elif self.path == "/events":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps(self._events)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"")

    def do_POST(self):
        if self.path == "/event":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data_string = self.rfile.read(int(self.headers['Content-Length']))
            self._events.append(json.loads(data_string))

    def do_DELETE(self):
        if self.path == '/reset':
            self._events = []
            self.send_response(HTTPStatus.OK)
            self.end_headers()


def main():
    hostName = "localhost"
    serverPort = 8080
    httpd = socketserver.TCPServer((hostName, serverPort), Handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    main()
