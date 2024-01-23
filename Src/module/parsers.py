
import json
from datetime import datetime
from config import *
# ? import asyncio Возможно будет асинхрон

# from codes import LATES_NEWS

class Parser:
    
    def __init__(self):
        print("init Parser")
        
        self.PATH_OPTIONS_PARSERS = '../data/parsers_instructions.json'
        self.parsers = self.load(self.PATH_OPTIONS_PARSERS)        

        self.parsing_report = {
            'web': {},
            'vk': {},
            'tg': {}
        }

        self.start_parsing()


    def load(self, path):
        with open(path, 'r') as file:
            return json.load(file)
        
    
    def now_str(self): return f"[{datetime.now()}]"
    

    # ? parsing - парсит web-сайты 
    def parsing_web(self) -> dict:
        if not self.parsing_report['web']:
            parsing_result = {
                'code': LATES_NEWS,
                'resource': 'web',
                'created': self.now_str(),
                'content': {
                    'msg': ['url', 'title', 'keywords'],
                    'err': ''
                }
            }
            self.parsing_report['web'] = parsing_result

    # ? parsing - парсит вк
    def parsing_vk(self) -> dict:
        if not self.parsing_report['vk']:
            parsing_result = {
                'code': LATES_NEWS,
                'resource': 'vk',
                'date': self.now_str(),
                'content': {
                    'msg': ['url\n', 'title\n', 'keywords\n'],
                    'err': ''
                }
            }
            self.parsing_report['vk'] = parsing_result

    
    # ? parsing - парсит telegram
    def parsing_tg(self) -> dict:
        if not self.parsing_report['tg']:
            parsing_result = {
                'code': LATES_NEWS,
                'resource': 'tg',
                'date': self.now_str(),
                'content': {
                    'msg': ['url', 'title', 'keywords'],
                    'err': ''
                }
            }
            self.parsing_report['tg'] = parsing_result
        
    
    def start_parsing(self):
        self.parsing_web()
        # self.parsing_vk()
        # self.parsing_tg()