class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases = "NULL"): #para crear un object #creo que null es para que sea
        #opcional pasar un argumento

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases #aquí es donde se crea
        if strbases == "NULL":
            print("NULL sequence created")
            self.strbases = "NULL"
        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR!")
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
        list_bases = ["A", "C", "G", "T"]
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        if self.strbases == "NULL" or self.strbases == "ERROR":
            list_count = [count_a, count_c, count_g, count_t]
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


