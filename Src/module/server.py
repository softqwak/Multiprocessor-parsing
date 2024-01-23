
from socket import *
from datetime import datetime
from config import *
from threading import Thread
from parsers import Parser
import json

class Server(Parser):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.request = {}
        self.server.bind(
            (self.host, self.port)
        )
        self.server.listen(1)
        print(self.server)

    def start(self):
        print('server start')
        while True:
            try:
                self.client, self.addr_client = self.server.accept()
                print('client connect')
                self.send_report(socket=self.client, code=SUCC_CONNECT)
                self.get_request(socket=self.socket)
                Thread(
                    target=self.keeping_connect, 
                    args=(self.client,),
                    daemon=True
                ).start()
            except Exception as e:
                print(str(e))            
        self.server.close()
    
    def now(self): return f'[{datetime.now()}]'
    
    def send_report(self, socket, code, report=None,err=None):        
        if report is None:
            report = {
                'code': code,
                'created': self.now(),
                'content': {
                    'msg': REPORT_MSG[code],
                    'err': err
                }
            }            
        print(report)
        report = json.dumps(report, ensure_ascii=False).encode(CODE)
        socket.send(report)
        
    def get_request(self, socket):
        self.request = json.loads(socket.recv(1024).decode(CODE))
        
    def keeping_connect(self, socket):

        def parsing() -> dict:
            parser = Parser()
            content = parser.start()
            
            print(f'{socket}\n{content}\n')
            for content_item in content:           
                print('sending report')
                print(f'\t{content_item}\n')                
                self.send_report(socket=socket, code=content_item['code'], report=content_item)
                print('send report') 

        is_connect = True
        while is_connect:
            parsing()
                
        socket.close()


        



if __name__ == "__main__":
    Server(
        "127.0.0.1", 
        30825
    ).start()