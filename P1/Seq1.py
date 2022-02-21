class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases): #para crear un object

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases #aquí es donde se crea
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR!")
        else:
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
        #we are going to use a dynamic method

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)