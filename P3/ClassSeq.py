class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases = "NULL"): #para crear un object #creo que null es para que sea
        #opcional pasar un argumento

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases #aquí es donde se crea
        if strbases == "NULL":
            print("NULL sequence created!")
            self.strbases = "NULL"
        #elif not self.valid_sequence():
            #self.strbases = "ERROR"
            #print("Invalid sequence created!")
        else:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self): #para imprimir las sequencias
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def len(self):
        """Calculate the length of the sequence"""
        new_len = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            new_len = 0
        else:
            new_len = len(self.strbases)
        return new_len

    def count_base(self):
        print("Sequence: ", self.strbases)
        print("Total lenght: ", len(self.strbases))
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for b in self.strbases:
            d[b] += 1
        total = sum(d.values())
        for k, v in d.items():
            d[k] = [v, (v * 100) / total]
        final_dict = d
        message = ""
        for k, v in final_dict.items():
            message += k + ": " + str(v[0]) + " (" + str(round(v[1], 2)) + "%)" + "\n"
        return message

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

    def read_fasta(self, filename):
        try:
            FOLDER = "./sequences/"
            full_seq = open(FOLDER + str(filename) + ".txt" , "r").read()
            full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
            return full_seq

        except FileNotFoundError:
            print("File does not exist. Choose another file.")


    #def seq_read_fasta(self, filename):
        #from pathlib import Path
        #file_contents = Path(filename).read_text()
        #lines = file_contents.splitlines()
        #body = lines[1:]
        #self.strbases = ""
        #for lines in body:
            #self.strbases += lines



