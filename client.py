from socket import socket, AF_INET, SOCK_STREAM
from pickle import dumps, loads

server = socket(AF_INET, SOCK_STREAM)
server.connect(("192.168.1.79", 4000))

def send(data): # Sends encrypted data to server
    server.send(dumps(data))

def recive(data_length: int = 1024): # Decodes encrypted data recive from server
    return loads(server.recv(data_length))

if __name__ == "__main__":
    username = input("What would you like to be called? ")
    send(username)
    while True:
        pass