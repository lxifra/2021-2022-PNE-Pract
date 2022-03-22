class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK!")

    def __str__(self):
        phrase = "Connection to SERVER at " + str(self.ip) + " PORT: " + str(self.port)
        return phrase

    def talk(self, msg):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response

    def info_operation(self, arg):
        print("Sequence: ", arg)
        print("Total lenght: ", len(arg))
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for b in arg:
            d[b] += 1
            print(b, ":", d[b], "(", (d[b] * 100) / len(arg), ")")

