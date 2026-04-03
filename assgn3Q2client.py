from socket import *
serverName = 'localhost'
serverPort = 42067

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
print("Client successfully connected!")

while True:
    userChoice = input('Type y to proceed and n to exit')
    if userChoice != 'y' and userChoice != 'n':
        print("Please enter a valid choice")
        continue
    elif userChoice == 'n':
        break
    inputDatagram = input('Enter the datagram to be sent : ')
    clientSocket.sendto(inputDatagram.encode(), (serverName, serverPort))
    receivedDatagram, addr = clientSocket.recvfrom(1024)
    print(f"Reversed input string from server address {addr} is : {receivedDatagram.decode()}")

clientSocket.close()