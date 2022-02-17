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

def seq_len():
    list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
    list_lenght = []
    FOLDER = "./sequences/"
    for l in list_genes:
        filename = l
        seq = open(FOLDER + filename, "r").read()
        lenght = len(seq)
        list_lenght.append(lenght)
    gene_lenght = list(zip(list_genes, list_lenght))
    return gene_lenght

def seq_count_base(seq):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for b in seq:
        if b == "A":
            count_a += 1
        elif b == "C":
            count_c += 1
        elif b == "G":
            count_g += 1
        elif b == "T":
            count_t += 1
    return count_a, count_c, count_g, count_t

def seq_count(seq):
    list_bases = ["A", "C", "G", "T"]
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for b in seq:
        if b == "A":
            count_a += 1
        elif b == "C":
            count_c += 1
        elif b == "G":
            count_g += 1
        elif b == "T":
            count_t += 1
    list_count = [count_a, count_c, count_g, count_g, count_t]
    new_dict = dict(zip(list_bases, list_count))
    return new_dict


