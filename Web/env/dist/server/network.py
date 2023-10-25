import socket


class Network:
    def __init__(self, HOST, PORT):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (HOST, PORT)
 
        self.id = self.connect()
        
        self.closed = False

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(1024).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(1024).decode()
        except socket.error as e:
            print(e)
            self.closed = True