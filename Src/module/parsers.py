
import json
from datetime import datetime
import asyncio

# from codes import LATES_NEWS

class Parser:
    
    def __init__(self):
        print("init Parser")
        
        self.PATH_OPTIONS_PARSERS = '../data/options_parsers.json'
        self.parsers = self.load(self.PATH_OPTIONS_PARSERS)        

        self.ioloop = asyncio.get_event_loop()
        self.ioloop.run_until_complete(self.start(self.ioloop))
        self.ioloop.close()

        asyncio.run(
            self.start(parsers=self.parsers)
        )
        

    def load(self, path):
        with open(path, 'r') as file:
            return json.load(file)
        
    
    def now_str(self): return f"[{datetime.now()}]"
    

   
        