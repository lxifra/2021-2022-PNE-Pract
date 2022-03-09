import socket


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "localhost"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

while True:
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        #print("Waiting for Clients to connect")\
        #(cs, client_ip_port) = ls.accept()

        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip()
        splitted_cmd = msg.split(" ")
        cmd = splitted_cmd[0]
        if cmd != "PING":
            arg = splitted_cmd[1]
        print(cmd)
        print(f"Message received: {msg}")
        if cmd == "PING":
            response = "OK\n"
        else:
            response = "HELLO. I am the Happy Server :-)\n"
        cs.send(response.encode())
        cs.close()