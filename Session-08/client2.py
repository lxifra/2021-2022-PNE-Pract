import socket
import termcolor
import colorama

# SERVER IP, PORT
IP = "192.168.1.45"
PORT = 8080

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
colorama.init()
print(colorama.Fore.RED + msg.decode("utf-8"))
termcolor.cprint(msg.decode("utf-8"), "green")

# Closing the socket
s.close()