import socket
import threading


class Server:
    def __init__(self,host,port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host,port))
        self.server.listen()

        self.clients = []

    def sends_messages(self,message):
        for client in self.clients:
            try:
                client.send(message)
            except:
                self.clients.remove(client)

    def waiting_messages(self, client):
        self.clients.append(client)
        while True:
            message = client.recv(1024)
            self.sends_messages(message)

    def start(self):
        print('server start')
        while True:
            client, addr = self.server.accept()
            print(addr,'client connected')
            client_wating_messages = threading.Thread(target=self.waiting_messages,args=(client,))
            client_wating_messages.start()

if __name__ == "__main__":
    server = Server('localhost',12345)
    server.start()