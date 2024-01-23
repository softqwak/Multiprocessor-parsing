
import json
from datetime import datetime
from config import *
# ? import asyncio Возможно будет асинхрон

# from codes import LATES_NEWS

class Parser:
    
    def __init__(self):
        print("init Parser")
        
        self.PATH_OPTIONS_PARSERS = '../data/options_parsers.json'
        self.parsers = self.load(self.PATH_OPTIONS_PARSERS)        

        self.parsing_report = {
            'web': {
                'code': REPORT,
                'date': self.now_str(),
                'content': ['url', 'title', 'keywords']
            },
            'vk': {},
            'tg': {}
        }


    def load(self, path):
        with open(path, 'r') as file:
            return json.load(file)
        
    
    def now_str(self): return f"[{datetime.now()}]"
    

    # ? parsing - парсит web-сайты 
    def parsing_web(self, parser: dict) -> dict:
        parsing_result = {
            'code': REPORT,
            'date': self.now_str(),
            'content': ['url', 'title', 'keywords']
        }
        self.parsing_report['web'] = parsing_result

    # ? parsing - парсит вк
    def parsing_vk(self, parser: dict) -> dict:
        parsing_result = {
            'code': REPORT,
            'date': self.now_str(),
            'content': ['url', 'title', 'keywords']
        }
        self.parsing_report['vk'] = parsing_result

    
    # ? parsing - парсит telegram
    def parsing_tg(self, parser: dict) -> dict:
        parsing_result = {
            'code': REPORT,
            'date': self.now_str(),
            'content': ['url', 'title', 'keywords']
        }
        self.parsing_report['tg'] = parsing_result
        
    
    def start(self, parsers) -> dict:
        ...