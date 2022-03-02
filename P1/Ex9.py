from Seq1 import Seq

s = Seq()
s.seq_read_fasta("../P0/sequences/FRAT1.txt")
print("Sequence: (Lenght: ", s.len(), ")", s)
print("Bases: ", s.count())
print("Rev: ", s.reverse())
print("Comp: ", s.complement())
