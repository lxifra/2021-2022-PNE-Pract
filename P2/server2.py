import socket
import termcolor

PORT = 8081
IP = "localhost"
MAX_OPEN_REQUESTS = 5

number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((IP, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()
        number_con += 1
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))
        msg = clientsocket.recv(2048).decode("utf-8")
        termcolor.cprint("Message from client: {}".format(msg), "yellow")
        message = "Hello from the teacher's server"
        send_bytes = str.encode(message)
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()