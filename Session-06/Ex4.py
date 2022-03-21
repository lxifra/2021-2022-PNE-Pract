import termcolor

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
        if seq_list == seq_list1:
            termcolor.cprint("Sequence" + str(n_list) + ": (Lenght: " + str(lenght) + ")" + seq.__str__(), "blue")
        elif seq_list == seq_list2:
            termcolor.cprint("Sequence" + str(n_list) + ": (Lenght: " + str(lenght) + ")" + seq.__str__(), "yellow")


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1)

print()
termcolor.cprint("List 2:", "yellow")
print_seqs(seq_list2)