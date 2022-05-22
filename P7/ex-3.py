import http.client
import json
import termcolor

gene = "MIR633"
ID = "ENSG00000207552"

SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + ID + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + ID + PARAMS)
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")

    info = r1.read().decode("utf-8")
    info = json.loads(info)

    termcolor.cprint("Gene: ", "green", end="")
    print(gene)
    termcolor.cprint("Description: ", "green", end="")
    print(info["desc"])
    termcolor.cprint("Bases: ", "green", end="")
    print(info["seq"])



except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()