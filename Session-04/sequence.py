from pathlib import Path
FILENAME = "ADA.txt"
seq_dna = Path(FILENAME).read_text()
head_seq = seq_dna.split("\n")[0]
body_seq = seq_dna.replace(head_seq, "")
body_seq = body_seq.replace("\n", "")
count_b = len(body_seq)
print("Number of total bases:", count_b)