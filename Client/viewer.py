from socket import socket, AF_INET, SOCK_STREAM
from pickle import loads
from os import _exit as exit

server = socket(AF_INET, SOCK_STREAM)
server.connect(("localhost", 4001))

if __name__ == "__main__":
    while True:
        data = server.recv(1024)
        data = loads(data)
        if not data: # Disconnected
            exit(1)
        else:
            data = loads(data)
            name = data["Name"]
            message = data["Message"]
            print(f"[{name}] {message}")