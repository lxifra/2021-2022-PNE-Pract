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

class Seq:

    def __init__(self, strbases = "NULL"):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        new_len = ""
        new_len = len(self.strbases)
        return new_len

    def count_base(self):
        listzip = []
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for bases in self.strbases:
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

        list_resource = self.path.split('?')
        path = list_resource[0]

        genes_dict = {
            "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
            "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
            "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
            "ANK2": "ENSG00000145362"
        }


        if path == "/":
            contents = read_html_file("html/index-medium.html").render(context={})


        elif self.path.startswith("/listSpecies?"):
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
                chromosome = arguments["chromosome"][0]
                classSpecies = request_json(ENDPOINT, specie)
                try:
                    if int(chromosome) >= len(classSpecies["top_level_region"]):
                        contents = read_html_file("html/error.html").render(
                            context={"msg": "The chromosome selected is not available."})
                    else:
                        chromosome_dict = classSpecies["top_level_region"][int(chromosome)]
                        lenght = chromosome_dict["length"]
                        contents = read_html_file("html/chromosomelenght.html").render(context={"c_lenght": lenght})
                except KeyError:
                    contents = read_html_file("html/error.html").render(
                        context={"msg": "The specie selected is not available."})
            except ValueError:
                contents = read_html_file("html/error.html").render(
                    context={"msg": "The chromosome selected is not available."})


        elif path == "/geneseq":
            ENDPOINT = "/sequence/id/"
            try:
                genename = arguments["gene"][0]
                id = genes_dict[genename]
                clasgen = request_json(ENDPOINT, id)
                sequence = clasgen["seq"]
                contents = read_html_file("html/geneseq.html").render(context={"genename": genename,
                                                                      "sequence": sequence})
            except KeyError:
                contents = read_html_file("html/error.html").render(
                    context={"msg": "The gene selected is not available."})


        elif path == "/geneinfo":
            ENDPOINT = "/sequence/id/"
            try:
                genename = arguments["gene"][0]
                id = genes_dict[genename]
                clasgen = request_json(ENDPOINT, id)
                chromosome = clasgen["desc"].split(":")
                print(chromosome)
                chromosome_name = chromosome[1]
                start = chromosome[3]
                end = chromosome[4]
                lenght = int(end) - int(start)
                contents = read_html_file("html/geneinfo.html").render(context={"start": start,
                                                                           "end": end,
                                                                           "lenght": lenght, "id": id,
                                                                           "chromosome": chromosome_name,
                                                                           "genename": genename})
            except KeyError:
                contents = read_html_file("html/error.html").render(
                    context={"msg": "The gene selected is not available."})

        elif path == "/genecalc":
            ENDPOINT = "/sequence/id/"
            try:
                genename = arguments["gene"][0]
                id = genes_dict[genename]
                clasgen = request_json(ENDPOINT, id)
                sequence = clasgen["seq"]
                total_len = len(sequence)
                gene_calc = Seq(sequence)
                gene_calc = Seq.count_base(gene_calc)
                contents = read_html_file("html/genecalc.html").render(context={"totallen": total_len,
                                                                      "genecalc": gene_calc})

            except KeyError:
                contents = read_html_file("html/error.html").render(
                    context={"msg": "The gene selected is not available."})


        elif path == "/genelist":
            ENDPOINT = "/phenotype/region/homo_sapiens/"
            try:
                chromo = arguments["chromosome"][0]
                start_point = arguments["start"][0]
                end_point = arguments["end"][0]
                param = str(chromo) + ":" + str(start_point) + "-" + str(end_point)
                genelist = []
                info_chromo = request_json(ENDPOINT, param)
                for total_dict in info_chromo:
                    for pheno_dict in total_dict["phenotype_associations"]:
                        if "attributes" in pheno_dict:
                            if "associated_gene" in pheno_dict["attributes"]:
                                a_dict = pheno_dict["attributes"]
                                genelist.append(a_dict["associated_gene"])
                            else:
                                pass
                if len(genelist) == 0:
                    contents = "Sorry, there are no associated genes in this region."
                else:
                    contents = read_html_file("html/genelist.html").render(context={"gene_list": genelist})

            except TypeError:
                contents = read_html_file("html/error.html").render(
                    context={"msg": "Resource is not available."})




        else:
            contents = read_html_file("html/error.html").render(
                context={"msg": "Resource is not available."})



        self.send_response(200)

        self.send_header('Content-Type', 'text/html3')
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