from socket import *
serverName = 'localhost'
serverPort = 42067

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print("Server is online!")

while True:
    receivedDatagram, addr = serverSocket.recvfrom(1024)
    decodedDatagram = receivedDatagram.decode()
    print(f"Connected to the client {addr} and received {decodedDatagram}")
    reversedDatagram = decodedDatagram[::-1]
    serverSocket.sendto(reversedDatagram.encode(), addr)