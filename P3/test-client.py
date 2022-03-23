import socket
from Classclient import Client

PRACTICE = 3
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "localhost"

print("Connection to SERVER at", IP, "PORT: ", PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
c = Client(IP, PORT)

#EXCERCISE 1:
print(" * TESTING PING...")
s.send(str.encode("PING"))
msg = s.recv(2048)
print(msg.decode("utf-8"))

#EXCERCISE 2:
print(" * TESTING GET...")
list = ["0", "1", "2", "3", "4"]
for n in list:
    msg = c.talk("GET " + n)
    print(msg)

seq = c.talk("GET 0")
seq = seq.split("GET 0:")[1]

#EXCERCISE 3:
print("* TESTING INFO...")
msg = c.talk("INFO " + seq)
print(msg)

#EXCERCISE 4:
print(" * TESTING COMP...")
msg = c.talk("COMP " + seq)
print(msg)

#EXCERCISE 5:
print(" * TESTING REV...")
msg = c.talk("REV " + seq)
print(msg)

#EXCERCISE 6:
print(" * TESTING GENE...")
genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for g in genes:
    msg = c.talk("GENE " + g)
    print(msg)

#EXCERCISE EXAM:
print(" * EXCERCISE PRACTICAL EXAM.")
sequence = input("Introduce a sequence: ")
msg = c.talk("OPE " + sequence)
s.close()


