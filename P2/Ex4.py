from Client0 import Client

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "localhost"
PORT = 8080
c = Client(IP, PORT)
print("Sending a message to the server...")
list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
for l in list_genes:
    seq = open(FOLDER + l, "r").read()
    response1 = c.talk("Sending...")
    response2 = c.talk(seq)
print(f"Response: {response2}")