from socket import *

ClientSocket =  socket(AF_INET, SOCK_STREAM)
ClientSocket.connect(('127.0.0',8000))

cmd = 'GET http://127.0.0.1/index.html HTTP/1.0\r\n\r\n'

ClientSocket.send(cmd.encode())

while True:
	data = ClientSocket.recv(500)
	if data<0:
		break;
	print(data.decode())
	
ClientSocket.close()





