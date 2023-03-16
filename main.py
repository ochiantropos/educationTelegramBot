import telebot
from abc import ABS, abstractclassmethod, abstractproperty, abstractmethod


class Main(object):
    
    __token = "5696755755:AAEJhesIzQLNeEm_SQTSV2uWKhfDhZXs2fU"
    __bot = None
    
    def __init__(self, *args):
        self.__bot = telebot.Telebot(self.__token)
        self.RunServise()
        
        
        
    def RunServise(self):
        pass
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        self.__bot.send_message(message.chat.id,"Привет ✌️ ")
        
    self.__bot.infinity_poling()


if __name__ == "__main__":
    Main()