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

def request_json(endpoint, parameter):
    SERVER = 'rest.ensembl.org'
    PARAMS = "?content-type=application/json"

    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", endpoint + parameter + PARAMS)
        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")

        info_dict = r1.read().decode("utf-8")
        info_dict = json.loads(info_dict)
        return info_dict

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()



class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        url = urlparse(self.path)
        arguments = parse_qs(url.query)

        list_resource = self.path.split('?')
        path = list_resource[0]

        contents = ""


        if path == "/":
            contents = read_html_file("html/index-basic.html").render(context={})


        elif path == "/listSpecies":
            ENDPOINT = "info/species"
            classSpecies = request_json(ENDPOINT, "")
            info_species = classSpecies["species"]
            list_names = []

            for c in info_species:
                list_names.append(c["display_name"])
            try:
                try:
                    limit = int(arguments["limit"][0])
                    wanted_names = list_names[0:int(limit)]
                except ValueError:
                    wanted_names = []
            except KeyError:
                limit = len(list_names)
                wanted_names = list_names[0:int(limit)]

            if len(wanted_names) == 0:
                contents = read_html_file("html/error.html").render(context={"msg": "The limit value is wrong."})
            else:
                contents = read_html_file("html/listSpecies.html").render(context={"limit": limit,
                                                                              "total_lenght": len(list_names),
                                                                              "wanted_list": wanted_names})

        elif path == "/karyotype":
            ENDPOINT = "info/assembly/"
            specie = arguments["specie"][0]
            classSpecies = request_json(ENDPOINT, specie)
            try:
                karyotype = classSpecies["karyotype"]
                contents = read_html_file("html/karyotype.html").render(context={"karyotype": karyotype})
            except KeyError:
                contents = read_html_file("html/error.html").render(context={
                    "msg": "The specie selected is not available."})


        elif path == "/lenght":
            ENDPOINT = "info/assembly/"
            try:
                specie = arguments["species"][0]
                chromosome = arguments["number"][0]
                classSpecies = request_json(ENDPOINT, specie)
                list_names = []
                try:
                    top_level_region = classSpecies["top_level_region"]
                    if int(chromosome) < 0:
                        contents = read_html_file("html/error.html").render(
                            context={"msg": "The chromosome selected is not available."})
                    else:
                        for elements in top_level_region:
                            length = elements["length"]
                            if "chromosome" in elements["coord_system"]:
                                name = elements["name"]
                                if int(length) >= int(chromosome):
                                    list_names.append(name)
                        if len(list_names) == 0:
                            contents = read_html_file("html/error.html").render(
                                context={"msg": "There are no chromosomes with a length bigger."})
                        else:
                            contents = read_html_file("html/chromosomelenght.html").render(
                                context={"list_names": list_names})
                except KeyError:
                    contents = read_html_file("html/error.html").render(
                        context={"msg": "The specie selected is not available."})
            except ValueError:
                contents = read_html_file("html/error.html").render(context={"msg": "The chromosome selected is not available."})



        else:
            contents = read_html_file("html/error.html").render(context={"msg": "Resource not available."})



        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()