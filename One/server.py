import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 55888))
s.listen(5)

while True:
    (clientsocket, address) = s.accept()
    
    print('connecti0n established')
    
    msg = 'This is the first socket mssg'
    clientsocket.send(bytes(msg, 'utf-8'))
    
    mssg = clientsocket.recv(1024)
    print(mssg)
    
    
    