import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 55888))

while True:
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    
    s.send(bytes('hey from client', 'utf-8'))