import Seq0

list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
for l in list_genes:
    seq = open(FOLDER + l, "r").read()
    full_seq = seq[seq.find("\n"):].replace("\n", "")
    new_dict = Seq0.seq_count(full_seq)
    print("Gene ", l.replace(".txt", ""), ":", new_dict)