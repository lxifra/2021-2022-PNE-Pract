#open a file, in FASTA format, and return a String with the DNA sequence

import Seq0
sequence = Seq0.seq_read_fasta()
print("The first 20 basis are: ")
print(sequence[0:20])
