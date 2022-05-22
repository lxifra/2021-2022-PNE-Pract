import http.client
import json

#genes_dict = {"SCRAP":"ENSG00000080603",
              #"FRAT1":" ENSG00000165879"} #BUSCAS "nombre gen" Ensembl stable identifier.


SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
ARG = "ENSG00000080603"
PARAMS = "?content-type=application/json"

print(f"\nConnecting to server: {SERVER}\n")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + ARG + PARAMS)

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print(f"CONTENT: {data1}")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()