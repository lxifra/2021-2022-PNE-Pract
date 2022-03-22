import socket
import termcolor
from ClassSeq import Seq

def info_operation(arg):
    print("Sequence: ", arg)
    print("Total lenght: ", len(arg))
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in arg:
        d[b] += 1
        print(b,  ":", d[b], "(" , (d[b] * 100) / len(arg),  ")")
        print("hola")



ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "localhost"

ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Message received: {msg}")

        split_list = msg.split(" ")
        cmd = split_list[0]

        #EXCERCISE 1:
        if cmd != "PING":
            arg = split_list[1]
        if cmd == "PING":
            response = "OK!"
            termcolor.cprint("PING COMMAND!", "yellow")
            print("OK!")


        #EXCERCISE 2:
        elif cmd == "GET":
            SEQUENCES = ["ADA.txt", "FRAT1.txt", "FXN.txt", "RNU6_269P.txt", "U5.txt"]
            FOLDER = "./sequences/"
            try:
                index = int(arg)
                filename = SEQUENCES[index]
                sequence = open(FOLDER + filename, "r").read()
                full_seq = sequence[sequence.find("\n"):].replace("\n", "")
                termcolor.cprint("GET", "yellow")
                print(full_seq)
                response = "GET " + str(index) + ":" + full_seq
                cs.send(response.encode())

            except ValueError:
                response = "The argument for the GET command must be a number from 0 to 4"
            except IndexError:
                response = "The argument for the GET command must be a number from 0 to 4"

        #EXCERCISE 3:
        #!!!!
        elif cmd == "INFO":
            termcolor.cprint("INFO", "yellow")
            response = info_operation(arg)

        #EXCERCISE 4:
        elif cmd == "COMP":
            termcolor.cprint("COMP", "yellow")
            sequence = Seq(arg)
            print("Seq: ", sequence)
            response = "COMP " + str(sequence.complement())
            print("Comp: ", response)

        #EXCERCISE 5:
        elif cmd == "REV":
            termcolor.cprint("REV", "yellow")
            reverse = arg[::-1]
            print(reverse)
            response = "REV " + str(reverse)

        elif cmd == "GENE":
            termcolor.cprint("GENE", "yellow")
            filename = Seq(arg)
            gene = filename.read_fasta(filename)
            print(gene)
            response = "GENE " + str(filename) + ":" + gene

        cs.send(response.encode())
        cs.close()