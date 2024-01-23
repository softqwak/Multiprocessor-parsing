
import telebot
from telebot import types
import json
from datetime import datetime
from config import *
from client import Client
from threading import Thread
import time
from keybind import KeyBinder

class Bot(Client):
    
    def load(self, path) -> dict:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def save(self, obj, path):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(obj, file)
    
    def now(self): return f'[{datetime.now()}]'
    
    def __init__(self):
        self.PATH_OPTIONS = '../data/options_bot.json'
        self.PATH_USERS = '../data/users.json'
        self.PATH_ANSWERS = '../data/answers.json'
        
        self.options = self.load(self.PATH_OPTIONS)
        self.users = self.load(self.PATH_USERS)['users']
        self.answers = self.load(self.PATH_ANSWERS)
        self.token = self.options['token']
        self.is_run = True

        # TODO: ошибка с дисплеем, возможно работает на винде
        KeyBinder.activate({
            'Ctrl-K': self.exit_command,
        },
        run_thread=True )

        self.getting_traffic = Thread(target=self.server_connect, args=(("127.0.0.1",30825),), daemon=True)
        self.thread_run = Thread(target=self.run, args=(), daemon=True)
        self.getting_traffic.start()
        self.thread_run.start()
        self.getting_traffic.join()
        self.thread_run.join()
    
    @staticmethod
    def exit_command(self):
        self.is_run = False
    

    def server_connect(self, connect_to):
        while True and self.is_run:
            super().__init__(connect_to)
            is_connect = self.connect()
            while not is_connect:
                is_connect = self.connect()
                time.sleep(0.1)

            print('server connect')
            while is_connect and self.is_run:
                try:
                    print("getting report")
                    self.get_report()
                    
                    print("get report")
                except Exception as e:
                    report = ''
                    print(e.args)
                    print(str(e))
                    if e.args[0] == 10054:
                        print('надо бы закрыть сокет и заново ждать подключение', end='')
                        self.socket.close()
                        is_connect = False
                        break
                
                if len(self.report) > 0:
                    print(f'client.report = {self.report}')
                    if self.report['code'] == LATES_NEWS:
                        users = self.load(self.PATH_USERS)['users']
                        for user in users:
                            if user['state'] == TRAFFIC_ON:
                                print(f'user:{user} get !!!!')
                                text = ''
                                for line in self.report['content']:
                                    text += line
                                self.send_message(int(user['id']), text)
                
                
        
    
    def run(self):
        self.bot = telebot.TeleBot(self.token)
        
        @self.bot.message_handler(commands=['start'])
        def get_command(message):
            self.chat = message.chat.id
            self.id_user = str(message.chat.id)
            print(f'{self.now()} user:{self.id_user} msg:{message.text}')
            if self.is_user(self.id_user) is not True: 
                return
            
            user = self.get_user(self.id_user)
            if user['auth'] == False:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(BTN_AUTH)
                btn2 = types.KeyboardButton(BTN_INFO)
                markup.add(btn1, btn2)
                
                answer = self.answers[START]
                self.send_message(message.chat.id, text=answer, reply_markup=markup)     
            else:
                self.set_state_user(self.id_user, MENU)
                self.menu(self.chat)
            
        @self.bot.message_handler(content_types=['text'])
        def get_message(message):
            self.chat = message.chat.id
            self.id_user = str(message.chat.id)
            print(f'{self.now()} user:{self.id_user} msg:{message.text}')
            
            if self.is_user(self.id_user) is not True: 
                return      

            user = self.get_user(self.id_user)
            
            # print(f'{self.now()} {self.is_traffic_on} {self.activate_traffic}')
            
            
            if user['state'] == START or user['state'] == INFO:            
                if message.text == BTN_INFO:
                    self.set_state_user(self.id_user, INFO)
                    self.info(self.chat)                    
                if message.text == BTN_AUTH:
                    self.set_state_user(self.id_user, AUTH)
                    self.auth(self.chat)                    
                    
            elif user['state'] == AUTH:
                
                if message.text == BTN_GET_ACCESSCODE:
                    self.get_accesscode(self.chat)                    
                if message.text == BTN_RESET_ACCESSCODE:
                    self.reset_accesscode(self.chat)    
                
                if message.text == user['accesscode']:
                    self.set_auth_user(self.id_user, True)
                    self.set_state_user(self.id_user, MENU)
                    self.menu(self.chat)
                    
            if user['state'] == MENU:    
                            
                if message.text == BTN_ON:
                    self.set_state_user(self.id_user, TRAFFIC_ON)
                    self.traffic_on(self.chat)
                    
                if message.text == BTN_SETTINGS:
                    self.settings(self.chat, self.id_user)
                    
            elif user['state'] == TRAFFIC_ON:
                
                if message.text == BTN_OFF:
                    self.set_state_user(self.id_user, MENU)
                    self.traffic_off(self.chat)
                    self.menu(self.chat)    
                                 
                if message.text == BTN_SETTINGS:
                    self.settings(self.chat, self.id_user)
                    
        self.bot.polling(none_stop=True, interval=0)
        
    def is_user(self, id_user):
        self.users = self.load(self.PATH_USERS)['users']
        for user in self.users:
            if user['id'] == id_user:
                return True
        return False

    def get_user(self, id_user):
        self.users = self.load(self.PATH_USERS)['users']
        for user in self.users:
            if user['id'] == id_user:
                return user
        return None
    
    def set_auth_user(self, id_user, auth):
        self.users = self.load(self.PATH_USERS)['users']
        for user in self.users:
            if user['id'] == id_user:
                user['auth'] = auth
                break
        self.save(
            obj = { 'users': self.users }, 
            path = self.PATH_USERS
        )    
        self.users = self.load(self.PATH_USERS)['users']
        print(f'{self.now()} user:{id_user} auth:{auth}')
        
    def set_state_user(self, id_user, state):
        self.users = self.load(self.PATH_USERS)['users']
        for user in self.users:
            if user['id'] == id_user:
                user['state'] = state
                break
        self.save(
            obj = { 'users': self.users }, 
            path = self.PATH_USERS
        )
        self.users = self.load(self.PATH_USERS)['users']
        print(f'{self.now()} user:{id_user} change state to:{state}')
        
    def auth(self, chat):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(BTN_GET_ACCESSCODE)
        btn2 = types.KeyboardButton(BTN_RESET_ACCESSCODE)
        markup.add(btn1, btn2)
        
        answer = self.answers[AUTH]
        self.send_message(chat, text=answer, reply_markup=markup)   
        
    def info(self, chat):
        answer = self.answers[INFO]
        self.send_message(self.chat, text=answer)       
        
    def get_accesscode(self, chat):
        answer = self.answers[GET_ACCESSCODE]
        self.send_message(chat, text=answer)   
        
    def reset_accesscode(self, chat):
        answer = self.answers[RESET_ACCESSCODE]
        self.send_message(chat, text=answer)   
        
    def menu(self, chat):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(BTN_ON)
        btn2 = types.KeyboardButton(BTN_SETTINGS)
        markup.add(btn1, btn2)
        
        answer = self.answers[MENU]
        self.send_message(chat, text=answer, reply_markup=markup)   
        
    def settings(self, chat, id_user):
        
        user = self.get_user(id_user)
        answer = self.answers[SETTINGS]
        answer += f'Версия программы парсинга - {user["settings"]["parser"]}\n'
        answer += f'Название базы данных - {user["settings"]["db"]}\n'
        answer += f'Сайты которые парсятся:\n'
        for website in user['settings']['websites']:
            answer += f'\t{website}\n'
        answer += f'Краткое описание заданных параметров - {user["settings"]["descript"]}'
        self.send_message(chat, text=answer)  
        
    def traffic_on(self, chat):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(BTN_OFF)
        btn2 = types.KeyboardButton(BTN_SETTINGS)
        markup.add(btn1, btn2)        
        answer = self.answers[TRAFFIC_ON]
        self.send_message(chat, text=answer, reply_markup=markup) 
        
        
    def traffic_off(self, chat):
        answer = self.answers[TRAFFIC_OFF]
        self.send_message(chat, text=answer) 
        
    def send_message(self, chat, text, reply_markup=None):
        print(f'{self.now()} user:{chat} get msg:{text}')
        self.bot.send_message(chat, text=text, reply_markup=reply_markup)
        
    
if __name__ == "__main__":
    Bot()