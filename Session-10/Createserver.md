- Step 1: Create the socket (Method socket())
- Step 2: Configure the socket: bind it to the remote IP and PORT (Method bind()
- Step 3: Configure the socket in listening mode (Method listen())
Main loop:
- Step 5: Wait for a client to connect (method accept())
- Step 6: When a client connects, the socket library creates a new socket for communicating with the client
- Step 7: Read the client messages. What does the client want? (metho rcv)
- Step 8: Process the request and send a response message (method send)