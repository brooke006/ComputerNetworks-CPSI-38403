#import socket module
from socket import *
import sys # In order to terminate the program


serverSocket = socket (AF_INET, SOCK_STREAM)
#Prepare a server socket

serverSocket.bind(('',6789))
serverSocket.listen(1)

while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
    
       message = connectionSocket.recv(1024).decode()
       filename = message.split()[1]
       f = open (filename[1:])
       outputdata = f.read()
       #Send one HTTP header line into socket
     
       connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
          
      #Send the content of the requested file to the client
       
       for i in range(0, len(outputdata)):
           connectionSocket.send(outputdata[i].encode())
           connectionSocket.send("\r\n".encode())

       connectionSocket.close()

    except IOError:
           
           #send response message for file not found
            
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("404 Not Found".encode())
    
            #close client socket

            connectionSocket.close()
    
    serverSocket.clsoe()

    sys.exit()#Termniate the program after sending the corresponding data