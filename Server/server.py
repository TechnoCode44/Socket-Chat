from socket import socket, AF_INET, SOCK_STREAM
from pickle import dumps, loads

server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 4000))
server.listen()

while True:
    client, address = server.accept()
    client.send(dumps("Hello, World"))