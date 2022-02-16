from pathlib import Path
FILENAME = "RNU6_269P.txt"
seq_dna = Path(FILENAME).read_text()
head_seq = seq_dna.split("\n")[0]
print("First line of the", FILENAME, "file:")
print(head_seq)
