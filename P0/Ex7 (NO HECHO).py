import Seq0

FOLDER = "./sequences/"
full_seq = open(FOLDER + "U5.txt", "r").read()
full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
seq = full_seq[0:20]
complement_seq = Seq0.seq_complement(seq)
print(seq)
print(complement_seq)