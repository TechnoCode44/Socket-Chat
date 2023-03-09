from socket import socket, AF_INET, SOCK_STREAM
from pickle import dumps, loads
from threading import Thread

server = socket(AF_INET, SOCK_STREAM)
server.connect(("192.168.1.79", 4000))

def send(data): # Sends encrypted data to server
    server.send(dumps(data))

def recive(data_length: int = 1024): # Recives data from server and prints it
    while True:
        data = server.recv(data_length)
        data = loads(data)
        name = data["Name"]
        message = data["Message"]
        print(f"[{name}] {message}")

if __name__ == "__main__":
    username = input("What would you like to be called? ")
    send(username)
    
    Thread(target=recive).start()

    while True:
        message = input("> ")
        send(message)