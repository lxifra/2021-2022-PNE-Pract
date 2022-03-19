from Client0 import Client

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "localhost"
PORT = 8080
c = Client(IP, PORT)
seq = open("./sequences/" + "FRAT1.txt", "r").read()
seq = seq[seq.find("\n"):].replace("\n", "")
print("Gene FRAT:", seq)

list_frag = []
count = 0
exit = False
frag = ""

for b in seq:
    frag += b
    if len(frag) == 10:
        print(frag)
    seq = seq[len(frag):]
    frag = ""






#print("Sending a message to the server...")
#response = c.talk("Testing!")
#print(f"Response: {response}")