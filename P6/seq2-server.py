import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

LIST_SEQUENCES = ["Seq0", "Seq1", "Seq2", "Seq3", "Seq4"]

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        print(self.path)

        if self.path == "/":
            contents = read_html_file("form-2.html").render(context={"n_sequences": len(LIST_SEQUENCES)})
            #el render para jinja es como el format para lo normal
        elif self.path == "/ping?":
            contents = Path("ping.html").read_text()
        elif self.path.startswith("/get?"):
            contents = read_html_file("get.html").render(context={"n_sequences": len(LIST_SEQUENCES)})



        #elif self.path.startswith("/echo?msg"):
            #message = self.path.split("?msg=")[1]
            #contents = Path("template.html").read_text().format(message.upper())
        else:
            contents = Path("error.html").read_text()



        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()