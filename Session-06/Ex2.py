class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

def print_seqs(seq_list):
    n_list = 0
    for seq in seq_list:
        lenght = len(seq.strbases)
        n_list += 1
        print("Sequence", n_list, ": (Lenght: ", lenght, ")", seq.__str__())


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print(print_seqs(seq_list))
