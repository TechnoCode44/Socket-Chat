from socket import socket
from pickle import dumps, loads

def client_handler(client: socket, viewers: list, address):
    def send_all(data): # Sends data to all viewers
        for viewer in viewers:
            viewer.send(dumps(data))

    def recive(data_length: int = 1024): # Decodes encrypted data recive from client
        return loads(client.recv(data_length))
    
    name = recive()
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
                "Name": name,
                "Message": message
            })

    print(f"[{address}] {name} disconnected")
    client.close()