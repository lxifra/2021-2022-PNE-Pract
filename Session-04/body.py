from pathlib import Path
FILENAME = "U5.txt"
seq_dna = Path(FILENAME).read_text()
head_seq = seq_dna.split("\n")[0]
body_seq = seq_dna.replace(head_seq, "")
print(body_seq)