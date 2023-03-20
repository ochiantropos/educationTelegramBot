import telebot

from pprint import pprint

from servise.InputServise import InputServise
from servise.CommandServise import CommandServise
import sys, os
import locale

# Встановлюємо кодування на utf-8
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Встановлюємо локаль на uk_UA.UTF-8
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')


servise_dir = (os.path.abspath(os.path.dirname(__file__)) + '/servise/')
servise_commands_dir = (os.path.abspath(os.path.dirname(__file__)) + '/servise/commands/')

sys.path.append(servise_dir)
sys.path.append(servise_commands_dir)



class Bot(object):
    __token = "5696755755:AAEJhesIzQLNeEm_SQTSV2uWKhfDhZXs2fU"
    __command_request = [None, None]
    __bot = None
    __instance = None
    __firt_run_command_init = False
    
    def __init__(self, __Token: str = ''):
        self.input_servie = InputServise("D:\\GitHub\\educationTelegramBot\\data")
        self.output_serise = CommandServise()
        if __Token == '':
            self.__bot = telebot.TeleBot(self.__token)
        else:
            try:
                self.__bot = telebot.TeleBot(__Token)
            except:
                self.__bot = telebot.TeleBot(self.__token)
                

        self.__autorize = self.__bot.message_handler(commands=['start'])(self.Start)
        self.__autorize = self.__bot.message_handler(commands=['почати'])(self.Start)
        
        self.Back_1 = self.__bot.message_handler(commands=["back"])(self.Back)
        self.Back_2 = self.__bot.message_handler(commands=["назад"])(self.Back)
       
        self.Close_1 = self.__bot.message_handler(commands=["close"])(self.Close)
        self.Close_2 = self.__bot.message_handler(commands=["закінчити"])(self.Close)
        
        self.__command = self.__bot.message_handler(content_types=['text'])(self.GetCommand)
        
        self.__bot.polling(none_stop=True, interval=0)
        
                
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Bot, cls).__new__(cls)
        return cls.__instance

    @staticmethod
    def get_instance():
        if not Bot.__instance:
            Bot()
        return Bot.__instance


    def Start(self, message):
        ansver = self.input_servie.Massage((message.text).replace("/", ""))
        self.__bot.send_message(message.chat.id, text=ansver)

    def Back(self, message):
        ansver = self.input_servie.BackTopPrev("en")
        self.__bot.send_message(message.chat.id, text=ansver)


    def GetCommand(self, message):
        
        
        if self.output_serise.status_of_command != True:
            ansver = self.input_servie.Massage(message.text)
            print(f"DebugLog: GetCommand >> ansver >> {ansver}")
            
            self.__command_request = self.output_serise.FilterAnsver(ansver)
            if self.output_serise.status_is_execute_command:
                print(f"DebugLog: GetCommand >> self.__command_request >> {self.__command_request[0]} {self.__command_request[1]}")
            
        else:
            
            self.output_serise.update_execute_to_command( message.text, self.__command_request[0], self.__command_request[1] )
        
        
        if self.output_serise.status_is_execute_command == True:
            
            if self.output_serise.status_of_command == True:
                if self.__firt_run_command_init == False:
                    self.output_serise.run_command_by_name(self.__command_request[0], self.__command_request[1])
                    if self.output_serise.status_of_command != False: 
                        self.__firt_run_command_init = True
                    else:
                        self.__firt_run_command_init = False
                        
                    
                self.__bot.send_message(message.chat.id, text=self.output_serise.last_ansver)

            else:
                self.output_serise.status_is_execute_command = False
                self.__firt_run_command_init = False
                self.__bot.send_message(message.chat.id, text=self.output_serise.last_ansver)
            
            
        else:
            self.__bot.send_message(message.chat.id, text=ansver)



if __name__ == "__main__":
    Bot()