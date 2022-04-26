import http.server
import socketserver
import termcolor
import pathlib

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        path = self.requestline.split(" ")[1]


        if path == "/" or path == "/index.html":
            contents = pathlib.Path("info/index.html").read_text()
        else:
            try:
                FILENAME = str(path) + ".html"
                contents = pathlib.Path(FILENAME.strip("/")).read_text()
            except FileNotFoundError:
                contents = pathlib.Path("info/error.html").read_text()


        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()