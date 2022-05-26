import http.client
import json
import termcolor


def request_json(endpoint, parameters):
    try:
        conn.request("GET", endpoint + parameters)
        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")

        info_dict = r1.read().decode("utf-8")

        if "json" in parameters:
            info_dict = json.loads(info_dict)
        else:
            pass

        return info_dict

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()


PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

try:
    data_listspecies = request_json("/listSpecies?", "limit=10&json=1")
    if type(data_listspecies) == dict:
        termcolor.cprint("DICT OF DATA_LISTSPECIES: ", "green")
        print(data_listspecies)
    else:
        termcolor.cprint("HTML OF DATA_LISTSPECIES: ", "green")
        print(data_listspecies)

    data_karyotype = request_json("/karyotype?", "specie=mouse&json=1")
    if type(data_karyotype) == dict:
        termcolor.cprint("DICT OF DATA_KARYOTYPE: ", "green")
        print(data_karyotype)
    else:
        termcolor.cprint("HTML OF DATA_KARYOTYPE: ", "green")
        print(data_karyotype)

    data_len = request_json("/lenght?", "species=mouse&chromosome=18&json=1")
    if type(data_len) == dict:
        termcolor.cprint("DICT OF DATA_LEN: ", "green")
        print(data_len)
    else:
        termcolor.cprint("HTML OF DATA_LEN: ", "green")
        print(data_len)

    data_geneseq = request_json("/geneseq?", "gene=FRAT1&json=1")
    if type(data_geneseq) == dict:
        termcolor.cprint("DICT OF DATA_GENESEQ: ", "green")
        print(data_geneseq)
    else:
        termcolor.cprint("HTML OF DATA_GENESEQ: ", "green")
        print(data_geneseq)

    data_geneinfo = request_json("/geneinfo?", "gene=FRAT1&json=1")
    if type(data_geneinfo) == dict:
        termcolor.cprint("DICT OF DATA_GENEINFO: ", "green")
        print(data_geneinfo)
    else:
        termcolor.cprint("HTML OF DATA_GENEINFO: ", "green")
        print(data_geneinfo)

    data_genecalc = request_json("/genecalc?", "gene=FRAT1&json=1")
    if type(data_genecalc) == dict:
        termcolor.cprint("DICT OF DATA_GENECALC: ", "green")
        print(data_genecalc)
    else:
        termcolor.cprint("HTML OF DATA_GENECALC: ", "green")
        print(data_genecalc)

    data_genelist = request_json("/genelist?", "chromosome=18&start=0&end=98765&json=1")
    if type(data_genelist) == dict:
        termcolor.cprint("DICT OF DATA_GENELIST: ", "green")
        print(data_genelist)
    else:
        termcolor.cprint("HTML OF DATA_GENELIST: ", "green")
        print(data_genelist)


except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
