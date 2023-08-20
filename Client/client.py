from socket import socket, AF_INET, SOCK_STREAM
from pickle import dumps
from os import _exit as exit

server = socket(AF_INET, SOCK_STREAM)
server.connect(("localhost", 4000))

def send(data): # Sends encrypted data to server
    server.send(dumps(data))

if __name__ == "__main__":
    username = input("What would you like to be called? ")
    send(username)

    while True:
        message = input("")
        send(message)

        if message == "/quit":
            exit(0)