sequence = "ACGTA"
sequence_name = "Sequence: " + sequence
sequence_lenght = "Total lenght: " + str(len(sequence))
d = {"A": 0, "C": 0, "G": 0, "T": 0}
message = ""
for bases in sequence:
    d[bases] += 1
total = sum(d.values()) #te da solo los valores sin las keys
for base, count in d.items():#te da tanto las keys como sus valores
    perc = str((count * 100) / total)
    d[base] = [str(count), str(perc)]
    message += str(base) + ": " + str(d[base][0]) + " (" + str((d[base][1])) + "%)" + "\n"

print(message)