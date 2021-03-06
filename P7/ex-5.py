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
            perc = str((count * 100) / total)
            termcolor.cprint(base + ": ", "blue", end="")
            print(count, "(", round(float(perc), 1), "%)", end="\n")
            listzip.append([count, base])
        termcolor.cprint("Most frequent base: ", "green", end="")
        print(max(listzip)[1])





import http.client
import json
import termcolor

SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"

genes_dict = {
    "FRAT1":"ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
              }

for genename, id in genes_dict.items():
    try:
        URL = SERVER + ENDPOINT + id + PARAMS
        print()
        print(f"Server: {SERVER}")
        print(f"URL: {URL}")

        conn = http.client.HTTPConnection(SERVER)

        try:
            conn.request("GET", ENDPOINT + id + PARAMS)
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")

            info = r1.read().decode("utf-8")
            info = json.loads(info)

            termcolor.cprint("Gene: ", "green", end="")
            print(genename)
            termcolor.cprint("Description: ", "green", end="")
            print(info["desc"])

            seq = info["seq"]
            sequence = Seq(seq)
            termcolor.cprint("Total lenght: ", "green", end="")
            print(Seq.len(sequence))
            count_base = Seq.count_base(sequence)

        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()
    except KeyError:
        print("Sorry, this name is not valid.")