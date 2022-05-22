import http.client
import json


SERVER = 'rest.ensembl.org'
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"Url: {URL}")

conn = http.client.HTTPConnection(SERVER)
#no usamos el port para que sea más seguro o algoasí, no lo necesitamos.

try:
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    #print(f"CONTENT: {data1}")

    if data1["ping"] == 1: #en formato string no funciona porq al usar ej json.loads intenta transformar
        # lo que le das al formato orginial o algo así.No necesitamos transformarlo, el json
        # ya lo hace por nosotros y lo mete en un diccionario o así.
        #QUESTION EXAM ^^^^

        print("PRINT OK! The database is running")
    else:
        print("ERROR! The database is not running")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
