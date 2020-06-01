import socket
class Device(object):
    """docstring for Device."""

    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def requestConnection(self,address,port):
        self.connection.connect((address,port))




class HostServer(object):
    """docstring for HostServer."""

    def __init__(self):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        self.csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.csocket.bind((HOST, PORT))
        self.acceptNewClient()

    def acceptNewClient(self,id = None):
        if id == None:
            self.csocket.listen()
            conn, addr = self.csocket.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

class Client(object):
    """docstring for Client."""

    def __init__(self):
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 65432        # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'Hello, world')
            data = s.recv(1024)

        print('Received', repr(data))
