import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 20202))

while True:
    data = s.recv(1024).decode()
    print(data)