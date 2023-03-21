from pprint import pprint
from servise.InputServise import InputServise
from servise.CommandServise import CommandServise

from extra_class.SeveManager import SaveManager

import sys, os, locale, json, telebot

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
    __base_dir_name = os.path.join(os.path.dirname(__file__), "data")
    __save_maneger : SaveManager
    __runtime_status = False

    _directory_to_save : str
    
    def __init__(self):
        # відкриваємо файл config.json і зчитуємо дані з нього
        with open('config.json') as f:
            config_data = json.load(f)

        # зчитуємо значення "token" та "directory_to_save" з об'єкту config_data
        token = config_data['token']
        directory_to_save = config_data['directory_to_save']
        
        self._directory_to_save = rf"{os.path.join(os.path.dirname(__file__),directory_to_save)}"
        
        if os.path.isdir(self._directory_to_save):
            
            self.__save_maneger = SaveManager(self._directory_to_save)
            self.input_servie = InputServise(self.__base_dir_name)
            self.output_serise = CommandServise()
            
            if token == '':
                self.__bot = telebot.TeleBot(self.__token)
            else:
                try:
                    self.__bot = telebot.TeleBot(token)
                except:
                    self.__bot = telebot.TeleBot(self.__token)

            self.__autorize1 = self.__bot.message_handler(commands=['start'])(self.Start)
            self.__autorize2 = self.__bot.message_handler(commands=['почати'])(self.Start)
            
            self.Back_1 = self.__bot.message_handler(commands=["back"])(self.Back)
            self.Back_2 = self.__bot.message_handler(commands=["назад"])(self.Back)
        
            self.Close_1 = self.__bot.message_handler(commands=["close"])(self.CloseEnAnsver)
            self.Close_2 = self.__bot.message_handler(commands=["закінчити"])(self.CloseUaAnsver)

            self.__command = self.__bot.message_handler(content_types=['text'])(self.GetCommand)
            
            self.__bot.polling(none_stop=True, interval=0)
            
        else:
            print(rf" the _directory_to_save = {self._directory_to_save} is not alowed dir to save the dialog ( check your config file )")
        

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance
    
    @staticmethod
    def get_instance():
        if not Bot.__instance:
            Bot()
        return Bot.__instance

    def __clear_proces(self):
        self.output_serise.status_is_execute_command = False
        self.output_serise.status_of_command = False
        self.__firt_run_command_init = False

    def Start(self, message):
        if self.__runtime_status == False:
            self.__start_answer(message)
            self.__runtime_status = True


    def __start_answer(self, message):
        ansver = self.input_servie.Massage((message.text).replace("/", ""))
        self.__save_maneger.SaveToHtml(message.text, ansver)
        self.__bot.send_message(message.chat.id, text=ansver)

    def Back(self, message):
        if self.__runtime_status:
            pprint(self.__base_dir_name)
            pprint(self.input_servie.linkManager.DataCategory.catalog_path)
            if self.__base_dir_name != self.input_servie.linkManager.DataCategory.catalog_path:
                if message.text == "/back":
                    ansver = self.input_servie.BackTopPrev("en")

                else:
                    ansver = self.input_servie.BackTopPrev("ua")

                self.__save_maneger.SaveToHtml(message.text, ansver)
                self.__bot.send_message(message.chat.id, text=ansver)
            else:
                if message.text == "/back":
                    ansver = "You are already in the last directory"
                else:
                    ansver = "Ви вже знаходитесь в останні директорії"
                self.__save_maneger.SaveToHtml(message.text, ansver)
                self.__bot.send_message(message.chat.id, text=ansver)

    def CloseUaAnsver(self, message):
        if self.__runtime_status:
            self.__clear_proces()
            ansver = "Виконання команди було закрито"
            self.__save_maneger.SaveToHtml(message.text, ansver)
            self.__bot.send_message(message.chat.id, text=ansver)
        
    def CloseEnAnsver(self, message):
        if self.__runtime_status:
            self.__clear_proces()
            ansver = "The execution of the command was closed"
            self.__save_maneger.SaveToHtml(message.text, ansver)
            self.__bot.send_message(message.chat.id, text=ansver)
        
    def GetCommand(self, message):
        if self.__runtime_status:
            print(f"DebugLog: GetCommand >> \n self.output_serise.status_is_execute_command {self.output_serise.status_is_execute_command} \n self.output_serise.status_of_command {self.output_serise.status_of_command} \n self.__firt_run_command_init {self.__firt_run_command_init}")

            if (message.text != "exit" and message.text != "/exit") and (message.text != "вихід" and message.text != "/вихід"):
                # strategy
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

                        self.__save_maneger.SaveToHtml(message.text, self.output_serise.last_ansver)
                        self.__bot.send_message(message.chat.id, text=self.output_serise.last_ansver)

                    else:
                        self.output_serise.status_is_execute_command = False
                        self.__firt_run_command_init = False
                        self.__save_maneger.SaveToHtml(message.text, self.output_serise.last_ansver)
                        self.__bot.send_message(message.chat.id, text=self.output_serise.last_ansver)

                else:
                    self.__save_maneger.SaveToHtml(message.text, ansver)
                    self.__bot.send_message(message.chat.id, text=ansver)

            elif message.text == "exit" or message.text == "/exit":
                ansver = "I was glad to chat, see you soon."
                self.__save_maneger.SaveToHtml(message.text, ansver)
                self.__bot.send_message(message.chat.id, text=ansver)
                self.__runtime_status = False
                self.__bot.stop_polling()

            else:
                ansver = "Радий був поспілкуватись, до зустрічі."
                self.__save_maneger.SaveToHtml(message.text, ansver)
                self.__bot.send_message(message.chat.id, text=ansver)
                self.__runtime_status = False
                self.__bot.stop_polling()


if __name__ == "__main__":
    Bot()

