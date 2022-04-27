import http.client
import json

genes_dict = {"SCRAP":"ENSG00000080603",
              "FRAT1":" ENSG00000165879"} #BUSCAS "nombre gen" Ensembl stable identifier.

#necesitas cambiar estos tres creo
SERVER = 'rest.ensembl.org'
ENDPOINT = "/info/ping" #necesitas cambiar el endpoint
PARAMS = "?content-type=application/json"

print(f"\nConnecting to server: {SERVER}\n")

conn = http.client.HTTPConnection(SERVER)
# no usamos el port para que sea más seguro o algoasí, no lo necesitamos.

try:
    conn.request("GET", ENDPOINT + PARAMS)
    # o endpoint + params o server+endpoint+params
    # usamos solo endpoint y params porq así funciona.
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print(f"CONTENT: {data1}")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()