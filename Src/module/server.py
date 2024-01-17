
from socket import *
from datetime import datetime
from codes import *
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
            print('reportnone')
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
            reports = parser.start()
            
            print(f'{socket}\n{reports}\n')
            for report in reports['reports']:           
                print('sending report')
                print(f'\t{report}\n')                
                self.send_report(socket=socket, code=reports['code'], report=report)
                print('send report') 

        is_connect = True
        while is_connect:
            parsing()
                
        socket.close()


        



if __name__ == "__main__":
    Server(
        "192.168.1.161", 
        30825
    ).start()