#count the bases of each gene.

import Seq0

list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "RNU6_269P.txt", "FXN.txt"]
FOLDER = "./sequences/"
for l in list_genes:
    seq = open(FOLDER + l, "r").read()
    full_seq = seq[seq.find("\n"):].replace("\n", "")
    final_list = Seq0.seq_count_base(full_seq)
    print("Gene: ", l.replace(".txt", ""))
    for v, b in final_list:
        print(b, ":", v)