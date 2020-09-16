# socket is the end-point that recieves data so with a socket we send and recieve data
# the socket its self is not the communication, it's just the end-point that recieves that communication
# and an end_point sits at and IP and PORT
import socket
import time
# picking in python is serialization(flattening) --> converting it to bytes
# what can we pickle in python? Objects(pretty much everything)
import pickle

HEADERSIZE = 10

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

    # how to handle sockets that exceed your buffer while you dont want to close the connection and want to let stream be open ? Header
    # header is gonna notify your program how long is your message and maybe give some other information
    # fixed length header
    
    # pickling
    d = {1: "Hey", 2: "there"}
    msg = pickle.dumps(d)
    
    # using header
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg


    #sending information to client socket object
    clientsocket.send(msg)

    '''
    # a quick example to see the connection is still open
    while True:
        time.sleep(3)
        msg = f"The time is! {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
    '''
