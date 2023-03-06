from socket import socket, AF_INET, SOCK_STREAM
from pickle import dumps, loads

server = socket(AF_INET, SOCK_STREAM)
server.connect(("192.168.1.79", 4000))

def send(data): # Sends encrypted data to server
    server.send(dumps(data))
