from Client0 import Client
import termcolor

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "localhost"
PORT = 8080
c = Client(IP, PORT)
list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
for l in list_genes:
    seq = open(FOLDER + l, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    msg = "Sending " + str(l.strip(".txt")) + " Gene to the server..."
    response1 = c.talk(msg)
    response2 = c.talk(seq)
    termcolor.cprint(f"To Server: {msg}", "blue")
    termcolor.cprint(f"From Server: {response1}", "yellow")
    termcolor.cprint(f"To Server: {seq}", "blue")
    termcolor.cprint(f"From Server: {response2}", "yellow")