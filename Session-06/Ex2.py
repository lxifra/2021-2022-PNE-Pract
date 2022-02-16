from seq1 import Seq

def print_seqs(seq_list):
    n_list = 0
    for s in seq_list:
        n_list += 1
        lenght = len(s.strbases)
        print("Sequence", n_list,": (Lenght: ", lenght,")", s)


#Sequence 0: (Length: 3) ACT
#prints their number in the list, their length and the sequence itself
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
file = print_seqs(seq_list)
