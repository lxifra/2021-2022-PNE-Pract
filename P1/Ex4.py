#lenght of invalid and null sequences

from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print("Sequence 1: (Lenght: ", s1.len(),")", s1)
print("Sequence 2: (Lenght: ", s2.len(),")", s2)
print("Sequence 3: (Lenght: ", s3.len(),")", s3)