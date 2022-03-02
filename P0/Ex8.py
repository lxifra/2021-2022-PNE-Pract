import Seq0

list_genes = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
list_max = []
for l in list_genes:
    seq = open(FOLDER + l, "r").read()
    full_seq = seq[seq.find("\n"):].replace("\n", "")
    final_list = Seq0.seq_count_base(full_seq)
    max_value = sorted(final_list)[-1]
    print(max_value)
    list_max.append(max_value)
list_2 = list(zip(list_genes, list_max))
print(list_max)
for g, small_list in list_2:
    print(small_list)
    print("Gene ", g.replace(".txt", ""), ": Most frequent base:", small_list[1])
