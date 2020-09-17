'''
import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tuple (a,b) is : IP and the PORT that we wish to connect to
# often the case the client will be remote to the server
# which means whith socket we can communicate to and from a python programs on the same machine
# on locally network set of machines
# or even remotely network machines
s.connect((socket.gethostname(), 1234))

while True:
    # buffering data
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg [HEADERSIZE:])

            d = pickle.loads(full_msg [HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

print(full_msg)
'''











# on a media connection: the client tells the server what their username is
# send message
# receive message
# in this project (for simpilicity) we have to either send a message or send an empty message to get an update 
import socket
import select
# we use this to match especific error codes
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
usernmae_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(usernmae_header + username)

while True:
    message = input(f"{my_username} > ")

    # if it's not empty
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    # regardless of wheter there is a message or not we want to update
    # we are gonna receive things until we hit an error
    try:
        while True:
            # receive things
            username_header = client_socket.recv(HEADER_LENGTH)
            # if we didnt get any data for whatever reason
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()
            # we want to convert username header to int
            username_length = int(usernmae_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f"{username} >  {message}")
    
    # when there are no more messages to be received (this case is fine but if it's not like this ...)
    except IOError as e:
        if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()
