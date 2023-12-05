import  socket

class Client_connection:
    def __init__(self):
        self.server_name = "127.0.0.1"
        self.port_number = 8080
        self.client_socket = socket.socket()

    def intilize_connection_to_server(self, request):
        self.client_socket.connect((self.server_name,self.port_number))
        self.client_socket.send(request.encode('utf-8'))
        modified_sentence = self.client_socket.recv(1024).decode()
        print(modified_sentence)
        self.client_socket.close()
        return