import telebot


class Bot(object):
    
    __token = "5696755755:AAEJhesIzQLNeEm_SQTSV2uWKhfDhZXs2fU"
    __bot = None
    
    def __init__(self, __Token: str = ''):
        if __Token == '':
            self.__bot = telebot.TeleBot(self.__token)
        else:
            try:
                self.__bot = telebot.TeleBot(self.__Token)
            except:
                self.__bot = telebot.TeleBot(self.__token)
                
        self.__autorize = self.__bot.message_handler(commands=["start"])(self.authorization)
        self.__bot.polling(none_stop=True, interval=0)
        
    def GetCommand(self, message):
        self.__bot.send_message(message.chat.id, "TEST")

    def SendAnsver(self,message, data):
        self.__bot.send_message(message.chat.id, data)
               

if __name__ == "__main__":
    Bot()