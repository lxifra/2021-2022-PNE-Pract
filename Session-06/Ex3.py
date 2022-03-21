class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases


def generate_seqs(pattern, number):
    sum = ""
    num_seq = []
    for i in range(1, number + 1):
        sum += pattern
        num_seq.append(sum)
    return num_seq

def print_seqs(seq_list):
    n_list = 0
    for seq in seq_list:
        lenght = len(seq)
        n_list += 1
        print("Sequence", n_list, ": (Lenght: ", lenght, ")", seq.__str__())

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)