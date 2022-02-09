import Seq0
def seq_ping():
    print("OK")

def seq_read_fasta():
    exit = False
    while not exit:
        filename = input("Insert a filename: ")
        try:
            FOLDER = "./sequences/"
            full_seq = open(FOLDER + filename, "r").read()
            full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
            exit = True
            return full_seq
        except FileNotFoundError:
            print("File does not exist. Choose another file.")

#def seq_read_fasta(filename):
    #FOLDER = "./sequences/"
    #full_seq = open(FOLDER + filename).read()
    #full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
    #return full_seq
