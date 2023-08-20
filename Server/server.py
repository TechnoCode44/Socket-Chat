from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from client_handler import *

clients = [] # List with clients object's
clients_data = []
viewers = []

def client_reciver():
    global client
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("0.0.0.0", 4000))
    server.listen()

    while True:
        client, address = server.accept()
        clients_data.append({})
        clients.append(client)
        Thread(target=client_handler, args=(client, viewers, address[0])).start()

def viewer_reciver():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("0.0.0.0", 4001))
    server.listen()

    while True:
        client, address = server.accept()
        viewers.append(client)
        Thread(target=client_handler, args=(client, viewers, address[0])).start()

if __name__ == "__main__":
    Thread(target=client_reciver).start()
    Thread(target=viewer_reciver).start()