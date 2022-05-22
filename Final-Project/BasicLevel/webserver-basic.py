import http.server
import http.client
import json
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        print("PATH:---- >", self.path)
        url = urlparse(self.path)
        termcolor.cprint(url, 'blue')
        arguments = parse_qs(url.query)
        termcolor.cprint(arguments, 'yellow')

        SERVER = 'rest.ensembl.org'
        PARAMS = "?content-type=application/json"

        if self.path == "/":
            contents = read_html_file("index-basic.html").render(context={})

        elif self.path.startswith("/listSpecies?"):
            ENDPOINT = "info/species"

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + PARAMS)
                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                classSpecies = r1.read().decode("utf-8")
                classSpecies = json.loads(classSpecies)
                species = classSpecies["species"]
                list_names = []
                limit = arguments["limit"][0]
                for c in species:
                    list_names.append(c["display_name"])
                    wanted_names = list_names[0:int(limit)]
                contents = read_html_file("listSpecies.html").render(context={"limit": limit,
                                                                              "total_lenght": len(list_names),
                                                                              "wanted_list": wanted_names})
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()


        elif self.path.startswith("/karyotype?"):
            contents = "WE HAVE ENTERED THE KARYOTYPE"
            ENDPOINT = "info/assembly/"
            specie = arguments["specie"][0]

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + specie + PARAMS)
                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                classSpecies = r1.read().decode("utf-8")
                classSpecies = json.loads(classSpecies)
                karyotype = classSpecies["karyotype"]
                contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype})
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()




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