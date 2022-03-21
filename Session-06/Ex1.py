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

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")