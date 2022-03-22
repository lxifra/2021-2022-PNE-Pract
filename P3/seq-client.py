import socket
from Classclient import Client

PORT = 8080
IP = "localhost"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
#s.send(str.encode("HELLO FROM THE CLIENT!!!"))

#EXCERCISE 1:
print(" * TESTING PING...")
s.send(str.encode("PING"))
msg = s.recv(2048)
print(msg.decode("utf-8"))

#EXCERCISE 2:
c = Client(IP, PORT)
#msg = c.talk("GET 2")


#EXCERCISE 3:
#print("* TESTING INFO...")
#msg = c.talk("INFO AACCGTAA")

#EXCERCISE 4:
#msg = c.talk("COMP ACGTA")

#EXCERCISE 5:
msg = c.talk("REV ACCTGT")
s.close()


