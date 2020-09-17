'''
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

    ''''''
    # a quick example to see the connection is still open
    while True:
        time.sleep(3)
        msg = f"The time is! {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
    ''''''

'''


# Handling multiple connections on the server side (broadcasting ...)
import socket
# managing many connection
# gives us operating system level io capabilities so on different os it's different
# because of that python has select that allows us to utilize that without needing to get into detailes
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

# key = clients' sockets
# value = user data
clients = {}

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        # if we didn't get any data, the client will close of the connection
        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        # someone just connected and we need to accept the connection and handle it
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            # someone just disconnected
            if user is False:
                continue

            sockets_list.append(client_socket)
            
            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
        
        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            
            user = clients[notified_socket]
            print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            # show this message for everybody
            for client_socket in clients:
                # we dont want to send it right back to the sender
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
