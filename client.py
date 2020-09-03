import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tuple (a,b) is : IP and the PORT that we wish to connect to
# often the case the client will be remote to the server
# which means whith socket we can communicate to and from a python programs on the same machine
# on locally network set of machines
# or even remotely network machines
s.connect((socket.gethostname(), 1234))

# 1024 buffer size
msg = s.recv(1024)
print(msg.decode("utf-8"))