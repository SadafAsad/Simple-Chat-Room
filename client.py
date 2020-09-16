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
