
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
    

    # ? parsing - парсит web-сайты 
    async def parsing_web(self, parser: dict) -> dict:
        print(f"запуск функции parsing_web to {parser}")
        parser_reports = [
            ['url: ...', 'title: ...']
        ]
        # ? здесь будут проходить этапы парсинга множества страниц на новостном ресурсе
        await asyncio.sleep(4)
        # ? ...
        print(f"возвращение в функцию parsing_web to {parser}")
        return parser_reports

    # ? parsing - парсит вк
    async def parsing_vk(self, parser: dict) -> dict:
        print(f"запуск функции parsing_web to {parser}")
        parser_reports = [
            ['url: ...', 'title: ...']
        ]
        # ? здесь будут проходить этапы парсинга множества страниц на новостном ресурсе
        await asyncio.sleep(4)
        # ? ...
        print(f"возвращение в функцию parsing_web to {parser}")
        return parser_reports
    
    async def start(self, parsers):
        tasks = [self.ioloop.create_task(self.parsing(parser=parser)) for parser in parsers]
        
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        result = done.pop().result()

        for pending_future in pending:
            pending_future.cancel()

        print(result)
        