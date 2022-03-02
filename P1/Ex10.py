from Seq1 import Seq
list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "../P0/sequences/"
list_max = []
for s in list_genes:
    seq = Seq()
    seq.seq_read_fasta("../P0/sequences/" + s)
    list_base = ["A", "C", "G", "T"]
    a, c, g, t = seq.count_base()
    list_count = [a, c, g, t]
    final_list = list(zip(list_count, list_base))
    max_value = sorted(final_list)[-1]
    list_max.append(max_value)
    list_2 = list(zip(list_genes, list_max))
    for g, small_list in list_2:
        pass
    print("Gene ", g.replace(".txt", ""), ": Most frequent base:", small_list[1])