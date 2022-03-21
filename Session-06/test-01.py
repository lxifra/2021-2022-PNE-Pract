from Seq0 import *

seq1 = "ATTCCCGGGG"

print(f"Seq:    {seq1}")
print(f"  Rev : {seq_reverse(seq1)}")
print(f"  Comp: {seq_complement(seq1)}")
print(f"  Length: {len(seq1)}")
print(f"    A: {count_bases(seq1, 'A')}")
print(f"    T: {count_bases(seq1, 'T')}")
print(f"    C: {count_bases(seq1, 'C')}")
print(f"    G: {count_bases(seq1, 'G')}")