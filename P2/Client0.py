class Client:
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

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid