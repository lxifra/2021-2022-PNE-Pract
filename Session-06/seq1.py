class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases = "NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL sequence created!")
            self.strbases = "NULL"
        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("Invalid sequence created!")
        else:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

#EXCERCISE 1:
    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

#EXCERCISE 2:


    def len(self):
        """Calculate the length of the sequence"""
        new_len = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            new_len = 0
        else:
            new_len = len(self.strbases)
        return new_len

    def count_base(self):
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        if self.strbases == "NULL" or self.strbases == "ERROR":
            pass
        else:
            for b in self.strbases:
                if b == "A":
                    count_a += 1
                elif b == "C":
                    count_c += 1
                elif b == "G":
                     count_g += 1
                elif b == "T":
                     count_t += 1
        return count_a, count_c, count_g, count_t

    def count(self):
        list_bases = ["A", "C", "G", "T"]
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        if self.strbases == "NULL" or self.strbases == "ERROR":
            list_count = [count_a, count_c, count_g, count_g, count_t]
            new_dict = dict(zip(list_bases, list_count))
        else:
            for b in self.strbases:
               if b == "A":
                   count_a += 1
               elif b == "C":
                    count_c += 1
               elif b == "G":
                     count_g += 1
               elif b == "T":
                     count_t += 1
        list_count = [count_a, count_c, count_g, count_g, count_t]
        new_dict = dict(zip(list_bases, list_count))
        return new_dict

    def reverse(self):
        reverse_seq = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            reverse_seq = self.strbases
        else:
            reverse_seq = self.strbases[::-1]
        return reverse_seq

    def complement(self):
        d = {"A": "T", "C": "G", "G": "C", "T": "A"}
        complement_seq = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            complement_seq = self.strbases
        else:
            for b in self.strbases:
                complement_seq += d[b]
        return complement_seq

    #def read_fasta(self):
        #exit = False
        #while not exit:
            #FILENAME = "U5.txt"
            #try:
                #FOLDER = "./sequences/"
                #full_seq = open(FOLDER + FILENAME, "r").read()
                #full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
                #exit = True
                #return full_seq
            #except FileNotFoundError:
                #print("File does not exist. Choose another file.")


    def seq_read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for lines in body:
            self.strbases += lines
