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

def count_bases(seq, base):
    count_base = 0
    for b in seq:
        if b == base:
            count_base += 1
    return count_base

def seq_reverse(file):
    reverse_seq = file[::-1]
    return reverse_seq

def seq_complement(seq):
    d = {"A": "T", "C": "G", "G": "C", "T": "A"}
    new_seq = ""
    for b in seq:
        new_seq += d[b]
    return new_seq
