from socket import socket
from pickle import dumps, loads

def client_handler(client: socket, clients_data: bool, clients: list, address):
    def send_all(data): # Sends data to all clients
        for client in clients:
            client.send(dumps(data))

    def recive(data_length: int = 1024): # Decodes encrypted data recive from client
        return loads(client.recv(data_length))
    
    clients_data["Name"] = recive()
    name = clients_data["Name"]
    send_all({
        "Name": "Server",
        "Message": f"{name} has joined the chat"
    })
    print(f"[{address}] {name} has connected")

    connected = True
    while connected:
        try:
            message = recive()
        except EOFError: # Unexpected disconnect (No data to pickle)
            connected = False
            send_all({
                "Name": "Server",
                "Message": f"{name} has broken there computer (L)"
            })
            continue
        
        if message == "/quit": # Disconnect message
            connected = False
            send_all({
                "Name": "Server",
                "Message": f"{name} has left the chat"
            })
        else:
            send_all({
                "Name": clients_data["Name"],
                "Message": message
            })

    print(f"[{address}] {name} disconnected")
    clients.remove(client)
    client.close()