from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from client_handler import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 4000))
server.listen()

clients_data = []

while True:
    client, address = server.accept()
    clients_data.append({})
    Thread(target=client_handler, args=(client, clients_data[-1])).start()