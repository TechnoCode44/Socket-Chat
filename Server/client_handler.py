from socket import socket
from pickle import dumps, loads

def client_handler(client: socket, clients_data: bool, clients: list):
    def send_all(data): # Sends data to all clients
        for client in clients:
            client.send(dumps(data))

    def recive(data_length: int = 1024): # Decodes encrypted data recive from client
        return loads(client.recv(data_length))
    
    clients_data["Name"] = recive()
    send_all({
        "Name": "Server",
        "Message": f"{clients_data['Name']} has joined the chat"
    })

    clients.remove(client)
    client.close()