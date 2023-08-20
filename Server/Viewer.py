from pickle import dumps

class Viewer:
    def __init__(self, client, address, clients) -> None:
        self.client = client
        self.address = address
        self.clients = clients

        print(f"[{address}] Viewer has connected")

    def send(self, data):
        try:
            encrpyted_data = dumps(data)
            self.client.send(encrpyted_data)
        except EOFError:
            print(f"[{self.address}] Viewer disconnected")
            self.client.close()
            self.clients.remove(self.client)