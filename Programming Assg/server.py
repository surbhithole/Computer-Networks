#import socket module

from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a socket

serverSocket.bind(('0.0.0.0', 1330))
serverSocket.listen(1)


while True:

#Establish the connection

	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
		print ("Received connection from : " + str(addr[0]))
		message = connectionSocket.recv(1024)         #####
		filename = message.split()[1]
		print (filename[1:])
		f = open(filename[1:])
		outputdata = f.read()
		f.close()

#Send one HTTP header line into socket


		connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

#Send the content of the requested file to the client

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		
		connectionSocket.close()
	except IOError:
#Send response message for file not found

		connectionSocket.send(b'HTTP/1.0 404 Page Not Found\r\n\r\n')
		connectionSocket.send(b'File ' + filename[1:] + b' Not found!!')
		connectionSocket.close()
#Close client socket

		#connectionSocket.close()

serverSocket.close()
