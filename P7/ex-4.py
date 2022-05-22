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
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        if self.strbases == "NULL" or self.strbases == "ERROR":
            pass
        else:
            for b in self.strbases:
                if b == "A":
                    count_a += 1
                elif b == "C":
                    count_c += 1
                elif b == "G":
                     count_g += 1
                elif b == "T":
                     count_t += 1
        return count_a, count_c, count_g, count_t

    def count(self):
        list_bases = ["A", "C", "G", "T"]
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        if self.strbases == "NULL" or self.strbases == "ERROR":
            list_count = [count_a, count_c, count_g, count_g, count_t]
            new_dict = dict(zip(list_bases, list_count))
        else:
            for b in self.strbases:
               if b == "A":
                   count_a += 1
               elif b == "C":
                    count_c += 1
               elif b == "G":
                     count_g += 1
               elif b == "T":
                     count_t += 1
        list_count = [count_a, count_c, count_g, count_g, count_t]
        new_dict = dict(zip(list_bases, list_count))
        return new_dict





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

genename = input("Insert the name of the gene: ")


try:
    id = genes_dict[genename]
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

        genename = Seq(genename)
        termcolor.cprint("Total lenght: ", "green", end="")
        seq = info["seq"]
        print(Seq.len(seq))



    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

except KeyError:
    print("Sorry, this name is not valid.")