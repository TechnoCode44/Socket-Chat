from socket import socket
from pickle import dumps, loads

def client_handler(client: socket, clients_data):
    def send(data): # Sends encrypted data to client
        client.send(dumps(data))

    def recive(data_length: int = 1024): # Decodes encrypted data recive from client
        return loads(client.recv(data_length))
    
    client.close()