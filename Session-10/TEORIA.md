The way the twos apps behaves in the communication depends on the model used. In the client-model, the initiative of the communications relies on the client, while the server is just waiting for clients to connect

We saw in the previous sessions that the client uses only one socket to connect to a server

In the case of Servers they need two sockets: One for listenning to the connections from the clients, and the other for transferring the data from/to the client, once the connection has been established

The communication process between the client and server is as follows:

- Step 1: Initial state.
- · The client has created a socket
- . The sever has created a socket and configured it in listening mode

- Step 2: The client start the connection (calling the connect() method in the socket)
- Step 3: The server creates another socket for communicating with the client.
- Step 4: The client and the server communicates normally, using the "blue" sockets. The "red" socket continues listening for new connection from other clients