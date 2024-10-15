import socket
import time
import threading

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.all_user = []
    
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(4)
        threading.Thread(target=self.ConnectHendler).start()
        print('Сервер запущен!')

    def ConnectHendler(self):
        while True:
            client, address = self.server.accept()
            print(1)
            if client not in self.all_user:
                print("Conect User!")
                self.all_user.append(client)
                threading.Thread(target=self.MassageHandler, args=(client,)).start()
                client.send("Вы подключены!".encode('utf-8'))
            time.sleep(2)

    def MassageHandler(self, client_socket):
        while True:
            message = client_socket.recv(1024)
            message = message.decode()
            for user in self.all_user:
                if user != client_socket:
                    user.send(message.encode('utf-8'))
            time.sleep(1)

MyServer = Server('127.0.0.1', 20202)
#26.205.223.55