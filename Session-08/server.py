import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #para crear un socket, poner siempre.
#AF_INET: el que se comunica con el IP
#SOCK_STREAM: los mensajes que se envian y se reciben

try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept() #para que el receptor acepte el mensaje del que
        #lo recibe

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        termcolor.cprint("Message from client: {}".format(msg), "yellow")

        # Send the messag
        message = "Hello from the teacher's server"
        #message = len(msg)
        #send_bytes = str(message).encode()
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()