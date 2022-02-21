class Seq:
    """A class for representing sequences"""

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

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR!")
        else:
            print("New sequence created!")

    #@staticmethod #para que la función no espere una class sino un argumento normal
    #def valid_sequence2(sequence):
        #valid = True
        #i = 0
        #while i < len(sequence) and valid:
            #c = sequence[i]
            #if c != "A" and c != "C" and c != "G" and c != "T":
                #valid = False
            #i += 1
        #return valid
    #Creo que es otra forma para hacer lo de abajo pero sin una clase o algo así

    #def valid_sequence(self):
        #valid = True
        #i = 0
        #while i < len(self.strbases) and valid:
            #c = self.strbases[i]
            #if c != "A" and c != "C" and c != "G" and c != "T":
                #valid = False
            #i += 1
        #return valid
        #we are going to use a dynamic method


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)