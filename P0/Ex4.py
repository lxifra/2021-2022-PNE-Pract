import Seq0

list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
for l in list_genes:
    seq = open(FOLDER + l, "r").read()
    full_seq = seq[seq.find("\n"):].replace("\n", "")
    a, c, g, t = Seq0.seq_count_base(full_seq)
    print("Gene ", l.replace(".txt", ""))
    print("A:", a)
    print("C:", c)
    print("G:", g)
    print("T:", t)
