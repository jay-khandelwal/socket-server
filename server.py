from socket import *

ServerSocket =  socket(AF_INET,SOCK_STREAM)
ServerSocket.bind(('localhost',8000))
ServerSocket.listen(5)
print('started server ......')
while True:
	(ClientSocket, address) = ServerSocket.accept()
	print(ClientSocket)
	print(address)
	rd = ClientSocket.recv(5000).decode()
	pieces = rd.split('\n')
	
	if len(pieces)>0:
		print(pieces)
		
	data = 'HTTP/1.1 200 OK\r\n'
	data += 'Content-Type: text/html; charset=utf-8\r\n'
	data += '\r\n'
	data += '<html><head><title>Example</title></head><body><p>This is an example of a simple HTML page with one paragraph.</p></body></html>\r\n\r\n'
	ClientSocket.sendall(data.encode())
	ClientSocket.shutdown(SHUT_WR)

ServerSocket.close()
print('Access http://localhost:8000')