import Seq0
gene_lenght = Seq0.seq_len()
for g, l in gene_lenght:
    print("Gene ", g.replace(".txt", ""), "---> Length:", l)