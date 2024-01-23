
from socket import *
from config import *
import json

class Client:
    
    def __init__(self, connect_to):
        print('client init')

        self.connect_to = connect_to
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.report = {}
        
    def connect(self):
        try:
            print('connecting')
            print(f'{self.connect_to}')
            self.socket.connect(self.connect_to)
            try:
                self.get_report()
            except Exception as e:
                self.report = ''
            
            if len(self.report) > 0:
                print(self.report)
                if self.report['code'] == SUCC_CONNECT:
                    return True            
        except ConnectionRefusedError:
            return False
        
        
            

    def get_report(self):
        self.report = json.loads(self.socket.recv(1024).decode(CODE))
        
    def send_request(self, request):
        request = json.dumps(request, ensure_ascii=False).encode(CODE)
        self.socket.send(request)
        
    