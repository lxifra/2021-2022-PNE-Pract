from Client0 import Client

PRACTICE = 2
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

seq = open("./sequences/" + "FRAT1.txt", "r").read()
seq = seq[seq.find("\n"):].replace("\n", "")
print("Gene FRAT:", seq)

frag = ""
seqnum = 0

for b in seq :
    frag += b
    if len(frag) == 10 and seqnum <= 9:
        seqnum += 1
        print("Fragment ", seqnum, ": ", frag)
        if seqnum % 2 == 0:
            PORT = 8080
            IP = "localhost"
            c = Client(IP, PORT)
            send = c.talk("Fragment " + str(seqnum) + ": " + frag)
        else:
            PORT = 8081
            IP = "localhost"
            c = Client(IP, PORT)
            send = c.talk("Fragment " + str(seqnum) + ": " + frag)
        seq = seq[len(frag):]
        frag = ""