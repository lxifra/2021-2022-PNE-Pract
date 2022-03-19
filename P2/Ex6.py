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

msg = c.talk("Sending FRAT1 Gene to the server, in fragment of 10 bases... ")

frag = ""
seqnum = 0

for b in seq :
    frag += b
    if len(frag) == 10 and seqnum <= 4:
        seqnum += 1
        print("Fragment ", seqnum, ": ", frag)
        send = c.talk("Fragment " + str(seqnum) + ": " + frag)
        seq = seq[len(frag):]
        frag = ""
