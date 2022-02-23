from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
list_seq = [s1, s2, s3]
i = 0
for s in list_seq:
    print("Sequence", i, ": (Lenght: ", s.len(),")", s)
    dict_seq = s.count()
    print(dict_seq)
    i += 1