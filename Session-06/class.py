class Seq:
    """A class for representing sequences"""

    #Hasta aquí y con un pass sería una clase vacía

    def __init__(self, strbases):

        # Esta es la función que se llama cada vez que creamos un objeto (cuando solo tiene self)

        self.strbases = strbases

        # Cuando se le añade strbases, es para convertir  una string en un objeto para la clase
        # sigue siendo una string

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

    #La rueda hacia arriba significa que la función de str ya se ha llamado antes.


# --- Main program
# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")