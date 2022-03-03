from seq1 import Seq

seq1 = Seq("ATTCCCGGGG")

print(f"Seq:    {seq1}")
print(f"  Rev : {reverse(seq1)}")
print(f"  Comp: {complement(seq1)}")
print(f"  Length: {len(seq1)}")
print(f"    A: {count_base(seq1, 'A')}")
print(f"    T: {count_base(seq1, 'T')}")
print(f"    C: {count_base(seq1, 'C')}")
print(f"    G: {count_base(seq1, 'G')}")