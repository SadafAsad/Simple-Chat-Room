# socket is the end-point that recieves data so with a socket we send and recieve data
# the socket its self is not the communication, it's just the end-point that recieves that communication
# and an end_point sits at and IP and PORT
import socket

# defining socket object - with socket family type and actual type of socket (a,b) -
# ^^ if INET corresponds to IPV4 and SOCK_STREAM corresponds to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

# binding socket
# the tuple is and IP and a Port
# hosting the server on the same machine that we have the code
# socket.gethostname() = localhost
s.bind((socket.gethostname(), 1234))

# queue of 5
s.listen(5)

# listen forever
while True:

    # clientsocket = a socket object
    # address = ip address
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    #sending information to client socket object
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
