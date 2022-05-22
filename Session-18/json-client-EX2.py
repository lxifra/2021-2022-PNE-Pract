import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

# Print the information in the object
print()
names = person["Name"]
#NAMES: [{'Firstname': 'Troll', 'Lastname': 'Face'}, {'Firstname': 'Sax', 'Lastname': 'Guy'}]

ages = person["age"]

phonenumbers = person["phoneNumber"]
print("------PHONENUMBERS: ", phonenumbers)

termcolor.cprint("Total people in the data base: ", 'green', end='')
print(len(names))

for i, name in enumerate(names):

    termcolor.cprint("Name:", 'green', end="")
    print(name["Firstname"], name["Lastname"])

    termcolor.cprint("Age:", 'green', end="")
    print(ages[i])

    for n, num in enumerate(phonenumbers):
        if num["number"][i] == "0":
            pass
        else:
            termcolor.cprint("  Phone {}:".format(n), 'blue')
            termcolor.cprint("    Type: ", 'red', end='')
            print(num["type"])
            termcolor.cprint("    Number: ", 'red', end='')
            print(num["number"][i])