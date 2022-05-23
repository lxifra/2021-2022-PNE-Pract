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

def request_json(endpoint, parameters):
    SERVER = 'rest.ensembl.org'
    PARAMS = "?content-type=application/json"

    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", endpoint + parameters + PARAMS)
        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")

        info_dict = r1.read().decode("utf-8")
        info_dict = json.loads(info_dict)
        return info_dict

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

def count_base(seq):
    listzip = []
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for bases in seq:
        d[bases] += 1
    total = sum(d.values())
    for base, count in d.items():
        perc = (count * 100) / total
        base = base + ": "
        count = str(round(perc, 1)) + "%"
        listzip.append(base + count)
    return listzip


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        url = urlparse(self.path)
        arguments = parse_qs(url.query)

        genes_dict = {
            "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
            "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
            "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
            "ANK2": "ENSG00000145362"
        }


        if self.path == "/":
            contents = read_html_file("index-medium.html").render(context={})


        elif self.path.startswith("/listSpecies?"):
            ENDPOINT = "info/species"

            classSpecies = request_json(ENDPOINT, "")
            info_species = classSpecies["species"]
            list_names = []

            for c in info_species:
                list_names.append(c["display_name"])
            try:
                limit = arguments["limit"][0]
                wanted_names = list_names[0:int(limit)]
            except KeyError:
                limit = len(list_names)
                wanted_names = list_names[0:int(limit)]

            contents = read_html_file("listSpecies.html").render(context={"limit": limit,
                                                                              "total_lenght": len(list_names),
                                                                              "wanted_list": wanted_names})

        elif self.path.startswith("/karyotype?"):
            ENDPOINT = "info/assembly/"
            specie = arguments["specie"][0]
            classSpecies = request_json(ENDPOINT, specie)
            try:
                karyotype = classSpecies["karyotype"]
                contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype})
            except KeyError:
                contents = Path("error.html").read_text()


        elif self.path.startswith("/lenght?"):
            ENDPOINT = "info/assembly/"

            specie = arguments["species"][0]
            chromosome = arguments["chromosome"][0]
            classSpecies = request_json(ENDPOINT, specie)
            try:
                if int(chromosome) >= len(classSpecies["top_level_region"]):
                    contents = "This number is too big."
                else:
                    chromosome_dict = classSpecies["top_level_region"][int(chromosome)]
                    lenght = chromosome_dict["length"]
                    contents = read_html_file("chromosomelenght.html").render(context={"c_lenght": lenght})
            except KeyError:
                contents = Path("error.html").read_text()


        elif self.path.startswith("/geneseq?"):
            ENDPOINT = "/sequence/id/"
            try:
                genename = arguments["gene"][0]
                id = genes_dict[genename]
                clasgen = request_json(ENDPOINT, id)
                sequence = clasgen["seq"]
                contents = read_html_file("geneseq.html").render(context={"genename": genename,
                                                                      "sequence": sequence})
            except KeyError:
                contents = Path("error.html").read_text()


        elif self.path.startswith("/geneinfo?"):
            ENDPOINT = "/sequence/id/"
            try:
                genename = arguments["gene"][0]
                id = genes_dict[genename]
                clasgen = request_json(ENDPOINT, id)
                chromosome = clasgen["desc"]
                start = 0
                end = len(clasgen["seq"]) - 1
                lenght = len(clasgen["seq"])
                contents = read_html_file("geneinfo.html").render(context={"start": start,
                                                                           "end": end,
                                                                           "lenght": lenght, "id": id,
                                                                           "chromosome": chromosome,
                                                                           "genename": genename})
            except KeyError:
                contents = Path("error.html").read_text()

        elif self.path.startswith("/genecalc?"):
            ENDPOINT = "/sequence/id/"
            try:
                genename = arguments["gene"][0]
                id = genes_dict[genename]
                clasgen = request_json(ENDPOINT, id)
                sequence = clasgen["seq"]
                total_len = len(sequence)
                gene_calc = count_base(sequence)
                contents = read_html_file("genecalc.html").render(context={"totallen": total_len,
                                                                      "genecalc": gene_calc})

            except KeyError:
                contents = Path("error.html").read_text()


        elif self.path.startswith("/genelist?"):
            ENDPOINT = "info/assembly/"
            contents = "YOU MADE IT TO THE GENE LIST!"











        else:
            contents = Path("error.html").read_text()



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