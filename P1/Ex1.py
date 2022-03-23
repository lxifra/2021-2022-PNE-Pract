from Seq1 import Seq
sequence = Seq("ACTGA") #this are empty objects of the class
print_seq = Seq.__str__(sequence)
lenght = Seq.len(sequence)
print(f"Sequence 1: (Lenght:", lenght, ")", print_seq)
