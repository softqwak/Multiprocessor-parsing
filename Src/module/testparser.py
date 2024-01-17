
from parsers import Parser
from datetime import datetime
from pprint import pprint
import json

from multiprocessing import Process
from threading import Thread, Semaphore

from time import sleep
    
# ? Этот класс моделрирует класс Server: и метод keeping_connect 
class Test(Parser):
    
    def __init__(self):
        super().__init__()
        self.PATH_OPTIONS_PARSERS = '../data/options_parsers.json'

                    
        # pprint(self.parsers)
        # self.test()


    def load(self, path) -> dict:
        """load(path) - return json data"""
        with open(path, 'r') as file:
            return json.load(file)
        
    def test(self):

        self.sem = Semaphore(7)

        def printtime(name: str):
            self.sem.acquire()
            print(f'thread {name}: ', end='')
            for i in range(50):
                print(f'{i}', end='')
            print()
            sleep(1)
            self.sem.release()

        threads = [Thread(target=printtime, args=(str(i),), daemon=True) for i in range(6)]
        for th in threads:
            th.start()
        for th in threads:
            th.join()

    # ?  Реализация функции в классе Server
    def keeping_connect(self, socket='socketNone'):

        def parsing() -> dict:
            parser = Parser()
            reports = parser.start()
            
            print(f'{socket}\n{reports}\n')
            for report in reports['reports']:           
                print('sending report')
                print(f'\t{report}\n')                
                # self.send_report(socket=socket, code=reports['code'], report=report)
                print('send report') 

        is_connect = True
        while is_connect:
            parsing()
                
        # socket.close()    
        
if __name__ == "__main__":

    Test()
    