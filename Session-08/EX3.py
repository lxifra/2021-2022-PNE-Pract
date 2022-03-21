import socket

# SERVER IP, PORT
PORT = 8080
IP = "localhost"

exit = False

while not exit:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
    s.connect((IP, PORT)) #create a connection between the client and the server
    s.send(str.encode(input("Insert a message: "))) #send a message from client to server
    s.close() #close the socket.
    exit = True
